#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/mman.h>
#include <time.h>
#include <sys/time.h>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <stdint.h>
#include "Labeling.h"
using namespace std;

class Camera{
	private:
		void* camera_base;
		void* lwSdram_base;
		void* lwCameraIp_base;
		void* lwCameraIpRead_base;
		int fd;
		int fd_camera;
		volatile uint8_t *camera_addr;
		volatile uint16_t *lwSdram_addr;
		volatile uint32_t *lwCameraIp_addr;
		volatile uint32_t *lwCameraIpRead_addr;
	public:
		enum{
			BUTTON_DOWN,
			BUTTON_UP
		};

		int lbuttoon_flag;
		cv::Mat camera_mt;
		cv::Mat camera_bin;
		cv::Vec2d push_point;

		Camera(){
			if((fd = open("/dev/mem",(O_RDWR | O_SYNC))) == -1){
				printf("ERROR: could not open \"/dev/mem\"...\n");
				return;
			}
			fd_camera = open("/dev/mem",(O_RDONLY));
			lwSdram_base = mmap(NULL,0x10000,(PROT_READ | PROT_WRITE),MAP_SHARED,fd,0xFFC20000);
			lwCameraIp_base = mmap(NULL,0x10000,(PROT_READ | PROT_WRITE),MAP_SHARED,fd,0xFF202000);
			lwCameraIpRead_base = mmap(NULL,0x80,(PROT_READ | PROT_WRITE),MAP_SHARED,fd,0xFF200000);
			camera_base = mmap(NULL,0x960000,(PROT_READ),(MAP_PRIVATE | MAP_LOCKED),fd_camera,0x20000000);
			if(camera_base == MAP_FAILED){
				printf("ERROR: mmap() failed...\n");
				close(fd);
				return;
			}
			camera_addr = (volatile uint8_t*)camera_base;
			lwCameraIp_addr = (volatile uint32_t*)(lwCameraIp_base+1281*4);
			lwCameraIpRead_addr = (volatile uint32_t*)(lwCameraIpRead_base);
			lwSdram_addr = (volatile uint16_t*)(lwSdram_base+0x5080);
			
			*lwSdram_addr = 0xffff;
		}
		~Camera()
		{
			munmap(lwSdram_base,0x10000);
			munmap(lwCameraIp_base,0x10000);
			if(munmap(camera_base,0x20000) != 0){
				printf("ERROR: mumap() failed...\n");
			}
			close(fd);
		}
		void shutterRelease(){
			*lwCameraIp_addr = 0x0001;
		}
		void modeChange(int mode){
			*(lwCameraIp_addr+2) = mode;
		}
		void threshold(unsigned int th){
			*(lwCameraIp_addr+3) = th;
		}
		void hue_threshold(unsigned int th){
			*(lwCameraIp_addr+4) = th;
		}
		void hue_range(unsigned int th){
			*(lwCameraIp_addr+5) = th;
		}
		void sat_threshold_low(unsigned int th){
			*(lwCameraIp_addr+7) = th;
		}
		void sat_threshold_high(unsigned int th){
			*(lwCameraIp_addr+8) = th;
		}
		void light_threshold_low(unsigned int th){
			*(lwCameraIp_addr+9) = th;
		}
		void light_threshold_high(unsigned int th){
			*(lwCameraIp_addr+10) = th;
		}
		int getStatus(){
			return *(lwCameraIp_addr+1);
		}
		bool shutterWait(){
			while((*(lwCameraIp_addr+1))&0x0400 == 0x0000){
				printf("status = %x\n",(*(lwCameraIp_addr+1)));
			}
			while((*(lwCameraIp_addr+1))&0x0400 == 0x0400){
				printf("status = %x\n",(*(lwCameraIp_addr+1)));
			}
			while((*(lwCameraIp_addr+1))&0x0400 == 0x0000){
				printf("status = %x\n",(*(lwCameraIp_addr+1)));
			}
			//while((*(lwCameraIp_addr))&0x0001 == 0x0001);
			return true;
		}
		cv::Mat getImg(int cloneFlag){
			uint32_t frame = *(lwCameraIpRead_addr);
			if(frame == 0){
				frame = 7;
			}
			else{
				frame--;
			}
			//cout << "frame = " <<  frame << hex << endl;
			//printf("frame = 0x%x\n",frame);
			//camera_mt = cv::Mat(480,640,CV_8UC4,(void*)(camera_addr+frame*640*480*4));
			camera_mt = cv::Mat(480,640,CV_8UC4,(void*)(camera_addr+frame*640*480*4));
			//cv::cvtColor(camera_mt,camera_bin,CV_BGR2GRAY);
			//cv::resize(camera_bin,camera_bin,cv::Size(),0.5,0.5,cv::INTER_NEAREST);
			//camera_mt = cv::Mat(240,320,CV_8UC4,(void*)(camera_addr+frame*640*480*4));
			if(cloneFlag != 0)
			{
				return camera_mt.clone();
		
			}
			else{
				return camera_mt;
			}
		}
};
class BallDetect{
	private:
		cv::Mat element;
		int median_size;
		int morpho_n;
		int morpho;
		LabelingBS label;
	public:
		BallDetect(){
		
		}
		void setting(int argMedian_size,int argMorpho_n,
				int argMorpho=cv::MORPH_ERODE,
				int argMorho_x = 3,int argMorho_y = 3){
			median_size = argMedian_size;
			morpho_n = argMorpho_n;
			morpho = argMorpho;
			element = cv::getStructuringElement(cv::MORPH_RECT,cv::Size(argMorho_y,argMorho_x));
		}
		cv::Mat extraction(cv::Mat binImg){
			if(median_size != 0){
				cv::medianBlur(binImg,binImg,median_size);
			}
			for(int i;i < morpho_n;i++){
				cv::morphologyEx(binImg,binImg,morpho,element);
			}
			return binImg;
		}
		void labeling(cv::Mat binImg,int thSize1,int thSize2,
				cv::Point &center,cv::Point &point1,cv::Point &point2){
			cv::Mat labelImage(binImg.size(),CV_16SC1);
			label.Exec(binImg.data,(short*)labelImage.data,binImg.cols,binImg.rows,false,thSize1);
			center.x = -1;
			center.y = -1;
			for (int i = 0; i < label.GetNumOfResultRegions(); i++)
			{
				RegionInfoBS *regioninfo = label.GetResultRegionInfo(i);
				int x1, x2, y1, y2, w, h;
				regioninfo->GetMin(x1, y1);
				regioninfo->GetMax(x2, y2);
				w = x2 - x1;
				h = y2 - y1;
				float x, y;
				regioninfo->GetCenter(x, y);
				int center_x = (int)x;
				int center_y = (int)y;

				if((w > thSize2) && (h > thSize2)){
					point1.x = x1;
					point1.y = y1;
					point2.x = x2;
					point2.y = y2;
					center.x = center_x;
					center.y = center_y;
					return;
				}
			}
		}
		cv::Mat labeling_hard(cv::Mat binImg,int *maxLine,int *maxValue){
			int sumValue;
			cv::Vec4b pixData;
			int maxValueData = 0;
			int maxLineData;
			cv::Mat result_img = binImg.clone();
			for(int i = 0;i < 480;i++){
				pixData = binImg.at<cv::Vec4b>(i,638);
				sumValue = ((pixData[0] & 0xff) + ((pixData[1] << 8) & 0xff00));
				if((sumValue  > maxValueData) && (sumValue < 640*2)){
				//if((sumValue  > maxValueData)){
				//if((sumValue  > maxValueData)){
					maxValueData = sumValue; 
					maxLineData = i;
				}
				else{
				}
				if(sumValue > 640*2)
				{
					sumValue = 640;
					cv::line(result_img,cv::Point(640-sumValue,i),cv::Point(638,i),cv::Scalar(255,0,0));
				}
				else if(sumValue != 0){
					cv::line(result_img,cv::Point(640-sumValue,i),cv::Point(638,i),cv::Scalar(255,0,0));
				}
			}
			if(maxValueData > 30){
				*maxValue = maxValueData;
				*maxLine = maxLineData;
			}
			return result_img;
		}
};
class Servo{
	private:
		void *lwServo_base;
		int fd;
		volatile uint16_t *lwServo_addr;
		int nowAngle[4];
		int oldAngle[4];
		enum{
			SERVO_X,
			SERVO_Y
		};
	public:
		Servo(){
			if((fd = open("/dev/mem",(O_RDWR | O_SYNC))) == -1){
				printf("ERROR: could not open \"/dev/mem\"...\n");
				return;
			}
			lwServo_base = mmap(NULL,32,(PROT_READ | PROT_WRITE),MAP_SHARED,fd,0xFF200000);
			lwServo_addr = (volatile uint16_t*)(lwServo_base+0x80);
			if(lwServo_base == MAP_FAILED){
				printf("ERROR: mmap() failed...\n");
				close(fd);
				return;
			}
			nowAngle[0] = 120;
			nowAngle[1] = 120;
			nowAngle[2] = 120;
			nowAngle[3] = 120;
		}
		~Servo(){
			if(munmap(lwServo_base,32) != 0){
				printf("ERROR: mumap() failed...\n");
			}
			close(fd);
		}
		void setPeriod(int num ,int period){
			if(num > 3){
				return;
			}
			*(lwServo_addr+num) = period;
		}	
		void setCompare(int num,int cmp){
			if(num > 3){
				return;
			}
			*(lwServo_addr+4+num) = cmp; 
		}
		void setDivider(int div){
			*(lwServo_addr+8) = div; 
		}
		void angle(int num,int angle){
			oldAngle[num] = nowAngle[num];
			nowAngle[num] = angle;
			setDivider(2);
			setPeriod(num,37500);
			setCompare(num,(int)(74.074*angle+8750));
		}
		void init(int initangle1,int initangle2){
			setCompare(SERVO_X,0);
			setCompare(SERVO_Y,0);
			sleep(1);
			angle(SERVO_X,initangle1);
			angle(SERVO_Y,initangle2);
			//4777
		}
		void tracking(cv::Point nowPoint,cv::Point targetPoint,double p){
			oldAngle[SERVO_X] = nowAngle[SERVO_X];
			oldAngle[SERVO_Y] = nowAngle[SERVO_Y];
			if((nowPoint.x == -1) || (nowPoint.y == -1)){
				return;
			}
			cv::Point2f pData = (nowPoint - targetPoint) * p;
			if((nowAngle[SERVO_X]+pData.x  < 200) && (nowAngle[SERVO_X]+pData.x > 40)){
				nowAngle[SERVO_X] += pData.x;
			}
			if((nowAngle[SERVO_Y]-pData.y  < 200) && (nowAngle[SERVO_Y]-pData.y > 120)){
				nowAngle[SERVO_Y] -= pData.y;
			}
			angle(SERVO_X,nowAngle[SERVO_X]);
			angle(SERVO_Y,nowAngle[SERVO_Y]);
		}

};
void mouse_callback(int event,int x,int y,int flags,void* param){
	Camera* camera = static_cast<Camera*>(param);
	if(cv::EVENT_LBUTTONDOWN){
		camera->lbuttoon_flag = 0;
	}
	else {
		camera->lbuttoon_flag = 1;
	}
}
int main(int argc,char **argv)
{
	int hueMax = 50;
	int hueMin = 20;
	int saturatsion = 0;
	int brigtness = 0;
	int hardFlag = 0;
	cv::Mat camera_mt(480,640,CV_8UC4);
	cv::Mat camera_mt_reg(480,640,CV_8UC4);
	cv::Mat hsv_mt(480,640,CV_8UC3);
	cv::Mat hsv_bin;
	cv::Mat hist_bin;
	Camera camera;
	Servo servo;
	BallDetect ballDet;
	//cv::Mat element = cv::getStructuringElement(cv::MORPH_RECT,cv::Size(1,5));
	cv::namedWindow("camera",CV_WINDOW_AUTOSIZE);
	//cv::setMouseCallback("camera",mouse_callback,(void*)&camera);
	
	camera.threshold(18);
	camera.modeChange(0);
	camera.shutterRelease();
	servo.init(120,140);
	ballDet.setting(0,0,cv::MORPH_ERODE,1,3);
	unsigned int th = 0;
	unsigned int th_hd = 150;
	int mode = 0;
	camera.hue_threshold(th_hd);
	camera.hue_range(30);
	camera.sat_threshold_low(0);
	camera.sat_threshold_high(255);
	camera.light_threshold_low(0);
	camera.light_threshold_high(255);
	while(1){
		clock_t start = clock();
		struct timespec start_val;
		clock_gettime(CLOCK_MONOTONIC,&start_val);

		if(mode != 4){
			camera_mt = camera.getImg(1);
		}
		/*
			vector<cv::Mat> planes,color_sh;
			cv::split(camera_mt,planes);
			color_sh.push_back(planes[3]);
			color_sh.push_back(planes[2]);
			color_sh.push_back(planes[1]);
			cv::merge(color_sh,camera_mt);
			*/	
		if((mode == 4) && (hardFlag == 0)){
			camera_mt = camera.getImg(1);
			int maxValue,maxLine;
			hist_bin = ballDet.labeling_hard(camera_mt,&maxLine,&maxValue);
			cout << "maxValue = " << maxValue << endl;
			cv::cvtColor(camera_mt,hsv_bin,CV_BGR2GRAY);
			//cv::inRange(hsv_mt,cv::Vec3b(hueMin,saturatsion,brigtness),cv::Vec3b(hueMax,255,255),hsv_bin);
			cv::resize(hsv_bin,hsv_bin,cv::Size(),0.5,0.5,cv::INTER_NEAREST);
			cv::Mat labelImage(hsv_bin.size(),CV_16SC1);
			hsv_bin = ballDet.extraction(hsv_bin);
			cv::Point center,point1,point2;
			// labeling
			ballDet.labeling(hsv_bin,1000,40,center,point1,point2);
			
			servo.tracking(center,cv::Point(hsv_bin.cols*0.5,hsv_bin.rows*0.5),0.05);
			cv::rectangle(camera_mt, point1*2, point2*2, cv::Scalar(0, 0, 255));
			cv::line(camera_mt,cv::Point(0,maxLine),cv::Point(638,maxLine),cv::Scalar(255,0,0));
			//cv::imshow("camera",hsv_bin);
			cv::imshow("camera",hist_bin);
		}
		if((mode == 4) && (hardFlag == 1)){
			camera_mt_reg = camera.getImg(1);
			int maxValue,maxLine;
			ballDet.labeling_hard(camera_mt_reg,&maxLine,&maxValue);
			cout << "maxValue = " << maxValue << endl;
			cv::line(camera_mt,cv::Point(0,maxLine),cv::Point(638,maxLine),cv::Scalar(255,0,0));
			cv::imshow("camera",hsv_bin);
		}
			//if(camera.lbuttoon_flag == 0){

		cv::imshow("camera_trans",camera_mt);

		hardFlag = 0;
		char k = cv::waitKey(30);
		if(k == 27){
			break;
		}
		else if(k == 'a'){
			camera.lbuttoon_flag = 0;
		}
		else if(k == 'u'){
			camera.hue_range(20);
			if(th < 255-10){
				th++;
				camera.threshold(th);
			}
			if(th_hd < 255){
				th_hd++;
				camera.hue_threshold(th_hd);
			}
			else {
				th_hd = 0;
				camera.hue_threshold(th_hd);
			}
		}
		else if(k == 'd'){
			camera.hue_range(20);
			if(th > 0+10){
				th--;
				camera.threshold(th);
			}
			if(th_hd > 0){
				th_hd--;
				camera.hue_threshold(th_hd);
			}
			else {
				th_hd = 255;
				camera.hue_threshold(th_hd);
			}
		}
		else if(k == 'm'){
			if(mode < 4)
			{
				mode++;
				camera.modeChange(mode);
			}
			else{
				mode = 0;
				camera.modeChange(mode);
			}
		}
		else if(k == 'h'){
			hardFlag = 1;
		}
		else{
			camera.lbuttoon_flag = 1;
		}
		hueMin = th-10;
		hueMax = th+10;
		struct timespec end;
		clock_gettime(CLOCK_MONOTONIC,&end);
		long sec = end.tv_sec - start_val.tv_sec;
		long nsec = end.tv_nsec-start_val.tv_nsec;
		if(nsec < 0){
			sec--;
			nsec += 1000000000L;
		}
		double msec = sec*1000+nsec/1000000;
		//double time_diff = end.tv_sec-start_val.tv_sec;
		//printf("time = %6fms,%d\n",((double)(clock() - start) / CLOCKS_PER_SEC)*1000,th_hd);
		printf("time = %fms,%d,%d\n",msec,th_hd,th);
		//cout << "sts  = " << camera.getStatus() << hex << endl;
		/*
		uint16_t dot_data;
		for(int i = 0;i < 480;i+=10){
			//dot_data =	camera_mt.at<cv::Vec3b>(i,639)[0] 
			//			+ ((camera_mt.at<cv::Vec3b>(i,639)[1] << 8)&0xff00); 
			cout << dec << i << "=" << hex <<
				((int)camera_mt.at<cv::Vec4b>(i,640)[1]&0x3) <<
				(int)camera_mt.at<cv::Vec4b>(i,640)[0] 
				<< endl;
		}
		*/
	}
	cv::destroyAllWindows();
	return 0;
}

