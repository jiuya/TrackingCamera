# -*- coding: utf-8 -*-
import numpy as np
import cv2

class opencv_test:
	# 初期化
	def __init__(self,parent = None):
		self.file = file
	#ファイルを読み込み、BGRをRGBに変換する関数
	def open_pic(self,file):
		pic = cv2.imread(file)
		pic_color = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
		return pic,pic_color
	#Canny処理してエッジ検出した後に、元の画像と重ねる関数
	def canny(self,pic):
		img =cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(img,100,200)
		edges2 = np.zeros_like(pic)
		for i in (0,1,2):
			edges2[:,:,i] = edges
		add = cv2.addWeighted(pic,1,edges2,0.4,0)
		return add

if __name__ == '__main__':
	#以下はファイル単独でのテスト用コード
	file = "lena.jpg"
	a = opencv_test()
	b,c = a.open_pic(file)
	d = a.canny(b)
	cv2.imshow("",d)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
