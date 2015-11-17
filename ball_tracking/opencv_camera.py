# -*- coding: utf-8 -*-
import numpy as np
import cv2
import threading

class opencv_test(threading.Thread):
	# 初期化
	def __init__(self,parent = None):
		threading.Thread.__init__(self)
		self.file = file
		self.cap = cv2.VideoCapture(0)
	#Canny処理してエッジ検出した後に、元の画像と重ねる関数
	def canny(self,pic):
		img =cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(img,100,200)
		edges2 = np.zeros_like(pic)
		for i in (0,1,2):
			edges2[:,:,i] = edges
		add = cv2.addWeighted(pic,1,edges2,0.4,0)
		return add

	def run(self):
		while True:
			ret, frame = self.cap.read()
			add = self.canny(frame)
			cv2.imshow('camera capture', add)
			k = cv2.waitKey(1)
			if k == 27:
				break
		self.cap.release()

if __name__ == '__main__':
	#以下はファイル単独でのテスト用コード
	a = opencv_test()
	a.run()