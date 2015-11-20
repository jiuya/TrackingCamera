# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ball_tracking_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_Qt_CV_MainWindow(object):
	def setupUi(self, Qt_CV_MainWindow):
		Qt_CV_MainWindow.setObjectName(_fromUtf8("Qt_CV_MainWindow"))
		Qt_CV_MainWindow.resize(660, 283)
		Qt_CV_MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		Qt_CV_MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.centralwidget = QtGui.QWidget(Qt_CV_MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 100, 501, 122))
		self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
		self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.label = QtGui.QLabel(self.verticalLayoutWidget)
		self.label.setObjectName(_fromUtf8("label"))
		self.verticalLayout_3.addWidget(self.label)
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.horizontalLayout_2.addWidget(self.label_2)
		self.H_lcd = QtGui.QLCDNumber(self.verticalLayoutWidget)
		self.H_lcd.setObjectName(_fromUtf8("H_lcd"))
		self.horizontalLayout_2.addWidget(self.H_lcd)
		self.H_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
		self.H_edit.setObjectName(_fromUtf8("H_edit"))
		self.horizontalLayout_2.addWidget(self.H_edit)
		self.H_slider = QtGui.QSlider(self.verticalLayoutWidget)
		self.H_slider.setMaximum(260000)
		self.H_slider.setOrientation(QtCore.Qt.Horizontal)
		self.H_slider.setObjectName(_fromUtf8("H_slider"))
		self.horizontalLayout_2.addWidget(self.H_slider)
		self.verticalLayout_3.addLayout(self.horizontalLayout_2)
		self.horizontalLayout_3 = QtGui.QHBoxLayout()
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.horizontalLayout_3.addWidget(self.label_3)
		self.S_lcd = QtGui.QLCDNumber(self.verticalLayoutWidget)
		self.S_lcd.setObjectName(_fromUtf8("S_lcd"))
		self.horizontalLayout_3.addWidget(self.S_lcd)
		self.S_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
		self.S_edit.setObjectName(_fromUtf8("S_edit"))
		self.horizontalLayout_3.addWidget(self.S_edit)
		self.S_slider = QtGui.QSlider(self.verticalLayoutWidget)
		self.S_slider.setMaximum(254)
		self.S_slider.setOrientation(QtCore.Qt.Horizontal)
		self.S_slider.setObjectName(_fromUtf8("S_slider"))
		self.horizontalLayout_3.addWidget(self.S_slider)
		self.verticalLayout_3.addLayout(self.horizontalLayout_3)
		self.horizontalLayout_4 = QtGui.QHBoxLayout()
		self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
		self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.horizontalLayout_4.addWidget(self.label_4)
		self.V_lcd = QtGui.QLCDNumber(self.verticalLayoutWidget)
		self.V_lcd.setObjectName(_fromUtf8("V_lcd"))
		self.horizontalLayout_4.addWidget(self.V_lcd)
		self.V_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
		self.V_edit.setObjectName(_fromUtf8("V_edit"))
		self.horizontalLayout_4.addWidget(self.V_edit)
		self.V_slider = QtGui.QSlider(self.verticalLayoutWidget)
		self.V_slider.setMaximum(254)
		self.V_slider.setOrientation(QtCore.Qt.Horizontal)
		self.V_slider.setObjectName(_fromUtf8("V_slider"))
		self.horizontalLayout_4.addWidget(self.V_slider)
		self.verticalLayout_3.addLayout(self.horizontalLayout_4)
		self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
		self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(530, 100, 91, 121))
		self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
		self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
		self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
		self.verticalLayout.setContentsMargins(-1, 1, -1, 1)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.exec_button = QtGui.QPushButton(self.verticalLayoutWidget_2)
		self.exec_button.setMinimumSize(QtCore.QSize(80, 60))
		self.exec_button.setObjectName(_fromUtf8("exec_button"))
		self.verticalLayout.addWidget(self.exec_button)
		self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(260, 10, 91, 80))
		self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.show_button = QtGui.QPushButton(self.horizontalLayoutWidget)
		self.show_button.setObjectName(_fromUtf8("show_button"))
		self.horizontalLayout.addWidget(self.show_button)
		self.verticalLayoutWidget.raise_()
		self.verticalLayoutWidget_2.raise_()
		self.horizontalLayoutWidget.raise_()
		Qt_CV_MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(Qt_CV_MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 24))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		self.menuFile = QtGui.QMenu(self.menubar)
		self.menuFile.setObjectName(_fromUtf8("menuFile"))
		Qt_CV_MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(Qt_CV_MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		Qt_CV_MainWindow.setStatusBar(self.statusbar)
		self.actionQuit = QtGui.QAction(Qt_CV_MainWindow)
		self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
		self.menuFile.addAction(self.actionQuit)
		self.menubar.addAction(self.menuFile.menuAction())

		self.retranslateUi(Qt_CV_MainWindow)
		QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), Qt_CV_MainWindow.close)
		QtCore.QObject.connect(self.H_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.H_lcd.display)
		QtCore.QObject.connect(self.H_edit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.H_lcd.display)
		QtCore.QObject.connect(self.V_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.V_lcd.display)
		QtCore.QObject.connect(self.V_edit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.V_lcd.display)
		QtCore.QObject.connect(self.S_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.S_lcd.display)
		QtCore.QObject.connect(self.S_edit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.S_lcd.display)
		QtCore.QMetaObject.connectSlotsByName(Qt_CV_MainWindow)

	def retranslateUi(self, Qt_CV_MainWindow):
		Qt_CV_MainWindow.setWindowTitle(_translate("Qt_CV_MainWindow", "MainWindow", None))
		self.label.setText(_translate("Qt_CV_MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">HSV</span></p></body></html>", None))
		self.label_2.setText(_translate("Qt_CV_MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">H</span></p></body></html>", None))
		self.label_3.setText(_translate("Qt_CV_MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">S</span></p></body></html>", None))
		self.label_4.setText(_translate("Qt_CV_MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">V</span></p></body></html>", None))
		self.exec_button.setText(_translate("Qt_CV_MainWindow", "Execute", None))
		self.show_button.setText(_translate("Qt_CV_MainWindow", "Show", None))
		self.menuFile.setTitle(_translate("Qt_CV_MainWindow", "File", None))
		self.actionQuit.setText(_translate("Qt_CV_MainWindow", "Quit", None))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Qt_CV_MainWindow = QtGui.QMainWindow()
	ui = Ui_Qt_CV_MainWindow()
	ui.setupUi(Qt_CV_MainWindow)
	Qt_CV_MainWindow.show()
	sys.exit(app.exec_())

