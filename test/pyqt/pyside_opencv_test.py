# -*- coding: utf-8 -*-
from __future__ import with_statement

import numpy as np
import sys
from PyQt4 import QtCore,QtGui
import os
from pyqt_Opencv import Ui_Qt_CV_MainWindow
#opencv_testファイルの読み込み
from opencv_test import opencv_test

class DesignerMainWindow(QtGui.QMainWindow,Ui_Qt_CV_MainWindow):
    def __init__(self, parent = None):
        super(DesignerMainWindow, self).__init__(parent)
        self.ui = Ui_Qt_CV_MainWindow()
    	self.setupUi(self)
    	QtCore.QObject.connect(self.file_button,QtCore.SIGNAL("clicked()"),self.open_file)
    	#executeボタンクリック時にexe_canny関数を実行
    	QtCore.QObject.connect(self.exec_button,QtCore.SIGNAL("clicked()"),self.exe_canny)
    def open_file(self):
    	self.file = QtGui.QFileDialog.getOpenFileName()
        if file:
            self.file_edit.setText(self.file)
    	    self.scene = QtGui.QGraphicsScene()
    	    pic_Item = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(self.file))
    	    __width = pic_Item.boundingRect().width()
    	    __height = pic_Item.boundingRect().height()
    	    __x = self.pic_View.x()
    	    __y = self.pic_View.y()
    	    self.pic_View.setGeometry(QtCore.QRect(__x, __y, __width, __height))

    	    __main_x = int(__x + __width + 20)
    	    __main_y = int(__y + __height + 50)
    	    self.resize(__main_x,__main_y)
    	    self.scene.addItem(pic_Item)
    	    self.pic_View.setScene(self.scene)
    	    return file
     #exe_canny関数：opecvのcanny処理画像をQtのQPixmapに変換し描画
    def exe_canny(self):
    	    #opencv_testファイルからクラスの読み込み
    	    cv_test = opencv_test()
    	    #ファイルを読み込んでRとBを交換
    	    pic,pic2 = cv_test.open_pic(unicode(self.file))
    	    #エッジ検出
    	    self.cv_img = cv_test.canny(pic2)
    	    #画像の高さ、幅を読み込み
    	    height, width, dim = self.cv_img.shape
    	    #全ピクセル数
    	    bytesPerLine = dim * width
    	    #Opencv（numpy）画像をQtのQImageに変換
    	    self.image = QtGui.QImage(self.cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
    	    #QImageをQPixmapに変換し、アイテムとして読み込む
    	    pic_Item = QtGui.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(self.image))
    	    #画像を描画
    	    self.scene.addItem(pic_Item)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	dmw = DesignerMainWindow()
	dmw.show()
	sys.exit(app.exec_())
