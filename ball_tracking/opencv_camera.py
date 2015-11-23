# -*- coding: utf-8 -*-
import numpy as np
import scipy as sc
import cv2
import threading

class opencv_test(threading.Thread):
	# 初期化
	def __init__(self,parent = None):
		threading.Thread.__init__(self)
		self.file = file
		self.cap = cv2.VideoCapture(0)
		self.beta = 0.9
	#Canny処理してエッジ検出した後に、元の画像と重ねる関数
	def canny(self,pic):
		img =cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(img,100,200)
		edges2 = np.zeros_like(pic)
		for i in (0,1,2):
			edges2[:,:,i] = edges
		add = cv2.addWeighted(pic,1,edges2,0.4,0)
		return add
	def cvt_hsvbin(self,img):
		hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(hsv, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
		edges2 = np.zeros_like(img)
		for i in (0,1,2):
			edges2[:,:,i] = mask
		return edges2
	def run(self):
		while True:
			ret, frame = self.cap.read()
			add = self.cvt_hsvbin(frame)
			img = cv2.addWeighted(frame,1,add,self.beta,0)
			cv2.imshow('camera capture', img)
			k = cv2.waitKey(1)
			if k == 27:
				break
		self.cap.release()

class opencv_camera(threading.Thread):
	# 初期化
	def __init__(self,parent = None):
		threading.Thread.__init__(self)
		self.file = file
		self.cap = cv2.VideoCapture(0)
		self.beta = 0.9
	#Canny処理してエッジ検出した後に、元の画像と重ねる関数
	def canny(self,pic):
		img =cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(img,100,200)
		edges2 = np.zeros_like(pic)
		for i in (0,1,2):
			edges2[:,:,i] = edges
		add = cv2.addWeighted(pic,1,edges2,0.4,0)
		return add
	def cvt_hsvbin(self,img):
		hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(hsv, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
		edges2 = np.zeros_like(img)
		for i in (0,1,2):
			edges2[:,:,i] = mask
		return edges2
	def run(self):
		while True:
			ret, frame = self.cap.read()
			add = self.cvt_hsvbin(frame)
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
