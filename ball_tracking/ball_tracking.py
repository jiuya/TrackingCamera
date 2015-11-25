# -*- coding: utf-8 -*-
from __future__ import with_statement

import numpy as np
import sys
from PyQt4 import QtCore,QtGui
import os
import threading
from ball_tracking_ui import Ui_Qt_CV_MainWindow
#from opencv_camera import opencv_camera
from opencv_camera import opencv_test


class DesignerMainWindow(QtGui.QMainWindow,Ui_Qt_CV_MainWindow):
    def __init__(self, parent = None):
        super(DesignerMainWindow, self).__init__(parent)
        self.ui = Ui_Qt_CV_MainWindow()
    	self.setupUi(self)
        self.testCv = opencv_test()
        self.testCv.setDaemon(True)
        self.testCv.start()
    	#executeボタンクリック時にexe_canny関数を実行
    	QtCore.QObject.connect(self.exec_button,QtCore.SIGNAL("clicked()"),self.exe_canny)
        QtCore.QObject.connect(self.H_slider, QtCore.SIGNAL("valueChanged(int)"), self.H_slider_changed)
        QtCore.QObject.connect(self.S_slider, QtCore.SIGNAL("valueChanged(int)"), self.S_slider_changed)
        QtCore.QObject.connect(self.V_slider, QtCore.SIGNAL("valueChanged(int)"), self.V_slider_changed)
    def exe_canny(self):
        if self.testCv.beta < 1:
            self.testCv.beta += 0.1
        else:
            self.testCv.beta = 0
    def H_slider_changed(self,value):
        self.testCv.hue_value = value
    def S_slider_changed(self,value):
        self.testCv.s_max = value
    def V_slider_changed(self,value):
        self.testCv.v_max = value

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	dmw = DesignerMainWindow()
	dmw.show()
	sys.exit(app.exec_())
