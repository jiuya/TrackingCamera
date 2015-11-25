# -*- coding: utf-8 -*-
import numpy as np
from scipy import ndimage
import cv2
import threading

class opencv_test(threading.Thread):
	# 初期化
	def __init__(self,parent = None):
		threading.Thread.__init__(self)
		self.file = file
		self.cap = cv2.VideoCapture(0)
		self.beta = 0.9
		self.hue_value = 90.
		self.hue_range = 10.
		self.s_max = 0.
		self.v_max = 0.
	#Canny処理してエッジ検出した後に、元の画像と重ねる関数
	def canny(self,pic):
		img =cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(img,100,200)
		edges2 = np.zeros_like(pic)
		for i in (0,1,2):
			edges2[:,:,i] = edges
		add = cv2.addWeighted(pic,1,edges2,0.4,0)
		return add
	def cvt_hsv(self,img):
		hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		#mask = cv2.inRange(hsv, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
		return hsv
	def cvt_hsvBin(self,img):
		hue = self.cvt_hsv(img)
		bin_image = cv2.inRange(hue, np.array((self.hue_value-self.hue_range, 0.,0.)),np.array((self.hue_value+self.hue_range,self.s_max,self.v_max)))
		return bin_image
	def morph(self,bin):
		st = cv2.getStructuringElement(cv2.MORPH_RECT,(8,8))
		for i in range(0,10):
			bin = cv2.morphologyEx(bin,cv2.MORPH_OPEN,st)
		return bin
	def run(self):
		while True:
			ret, frame = self.cap.read()
			binImage = self.cvt_hsvBin(frame)
			opening = self.morph(binImage)
			label_image ,label_num = ndimage.label(opening)
			add = np.zeros_like(frame)
			for i in (0,2):
				add[:,:,i] = label_image*10
			img = cv2.addWeighted(frame,1,add,self.beta,0)
			cv2.imshow('camera capture', img)
			k = cv2.waitKey(1)
			if k == 27:
				break
		self.cap.release()

if __name__ == '__main__':
	#以下はファイル単独でのテスト用コード
	a = opencv_test()
	a.run()
