import os
import sys
import mmap
import numpy as np
import time
import cv2

class Camera:
    hwRegsSpan = 0x200000
    hwRegsBase = 0x20000000
    def __init__(self):
        self.fd = os.open("/dev/mem",os.O_RDWR | os.O_SYNC)
        self.lwSdramAddr = mmap.mmap(self.fd, 0x10000,
                mmap.MAP_SHARED,mmap.PROT_READ | mmap.PROT_WRITE,
                offset=0xFFC20000)
        self.lwCameraIpAddr = mmap.mmap(self.fd, 0x10000,
                mmap.MAP_SHARED,mmap.PROT_READ | mmap.PROT_WRITE,
                offset=0xFF201000)
        self.f2sCameraAddr = mmap.mmap(self.fd, Camera.hwRegsSpan,
                mmap.MAP_SHARED,mmap.PROT_READ | mmap.PROT_WRITE,
                offset=Camera.hwRegsBase)

        self.lwSdramAddr.seek(0x5080,os.SEEK_SET)
        self.lwSdramAddr.write_byte(chr(0xff))
        self.lwSdramAddr.write_byte(chr(0x3f))
        self.lwSdramAddr.close()
	
	self.update()

        self.img = np.zeros( (480,640,3),np.uint8 )
        self.w_range = range(0,640)
        self.h_range = range(0,480)
    def __del__(self):
        self.f2sCameraAddr.close()
        self.lwCameraIpAddr.close()
        os.close(self.fd)
    def update(self):
        self.lwCameraIpAddr.seek(1281*2,os.SEEK_SET)
        self.lwCameraIpAddr.write_byte(chr(0x1))
        self.lwCameraIpAddr.write_byte(chr(0x0))
        flag = 0
	while flag != 4:
            self.lwCameraIpAddr.seek((1282*2)+1,os.SEEK_SET)
            flag = ord(self.lwCameraIpAddr.read_byte()) & 4
    def writeData(self,wordData):
        self.f2sCameraAddr.write_byte(chr(wordData))
    def posReset(self,pos):
        self.f2sCameraAddr.seek(0+pos,os.SEEK_SET)
    def readData(self):
        return ord(self.f2sCameraAddr.read_byte())
    def read(self):
	self.update()
        self.posReset(0)
        for h in self.h_range:
            for w in self.w_range:
                hdata = self.readData()
                ldata = self.readData()
                self.img[h,w,0] = (ldata << 3) & 0xf8
                self.img[h,w,1] = ((ldata >> 3) & 0x1c) | ((hdata << 5) & 0xe0)
                self.img[h,w,2] = (hdata & 0xf8)
        return self.img
if __name__ == '__main__':
    camera = Camera()

    # h*w*bgr
    freq = 1000/cv2.getTickFrequency()

    while True :
        start_time = cv2.getTickCount()
        img = camera.read()
        diff_time = (cv2.getTickCount() - start_time)*freq
        print "get time : %fms" % diff_time
        cv2.imshow('camera capture', img)

        k = cv2.waitKey(0)
        if k == 27:
            break
        if k == ord("w"):
            for h in xrange(20):
                for w in xrange(640):
                    print "b%x " % img[h,w,0] ,
                    print "g%x " % img[h,w,1] ,
                    print "r%x " % img[h,w,2] ,
                print ""
    cv2.destroyAllWindows()
