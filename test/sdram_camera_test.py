import os
import sys
import mmap
import numpy as np
import time
import cv2

class Camera:
    hwRegsSpan = 0x200000
    hwRegsBase = 0xff200000
    def __init__(self):
        self.fd = os.open("/dev/mem",os.O_RDWR | os.O_SYNC)
        self.h2pLwCameraAddr = mmap.mmap(self.fd, Camera.hwRegsSpan,
                mmap.MAP_SHARED,mmap.PROT_READ | mmap.PROT_WRITE,
                offset=Camera.hwRegsBase)
        self.h2pLwCameraAddr.seek(0x100000,os.SEEK_SET)
        self.img = np.zeros( (480,640,3),np.uint8 )
        self.w_range = range(0,640)
        self.h_range = range(0,480)
    def __del__(self):
        self.h2pLwCameraAddr.close()
        os.close(self.fd)
    def writeData(self,wordData):
        self.h2pLwCameraAddr.write_byte(chr(wordData))
    def posReset(self,pos):
        self.h2pLwCameraAddr.seek(0x100000+pos,os.SEEK_SET)
    def readData(self):
        return ord(self.h2pLwCameraAddr.read_byte())
    def read(self):
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
