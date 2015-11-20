# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_Opencv.ui'
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
		Qt_CV_MainWindow.resize(660, 623)
		Qt_CV_MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		Qt_CV_MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.centralwidget = QtGui.QWidget(Qt_CV_MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.pic_View = QtGui.QGraphicsView(self.centralwidget)
		self.pic_View.setGeometry(QtCore.QRect(20, 180, 591, 331))
		self.pic_View.setMinimumSize(QtCore.QSize(591, 331))
		self.pic_View.setMaximumSize(QtCore.QSize(1000, 1000))
		self.pic_View.setMouseTracking(True)
		self.pic_View.setFocusPolicy(QtCore.Qt.NoFocus)
		self.pic_View.setAutoFillBackground(False)
		self.pic_View.setObjectName(_fromUtf8("pic_View"))
		self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 501, 89))
		self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
		self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.size_lcd = QtGui.QLCDNumber(self.verticalLayoutWidget)
		self.size_lcd.setObjectName(_fromUtf8("size_lcd"))
		self.horizontalLayout_2.addWidget(self.size_lcd)
		self.size_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
		self.size_edit.setObjectName(_fromUtf8("size_edit"))
		self.horizontalLayout_2.addWidget(self.size_edit)
		self.size_slider = QtGui.QSlider(self.verticalLayoutWidget)
		self.size_slider.setMaximum(260000)
		self.size_slider.setOrientation(QtCore.Qt.Horizontal)
		self.size_slider.setObjectName(_fromUtf8("size_slider"))
		self.horizontalLayout_2.addWidget(self.size_slider)
		self.verticalLayout_3.addLayout(self.horizontalLayout_2)
		self.horizontalLayout_3 = QtGui.QHBoxLayout()
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.threshold1_lcd = QtGui.QLCDNumber(self.verticalLayoutWidget)
		self.threshold1_lcd.setObjectName(_fromUtf8("threshold1_lcd"))
		self.horizontalLayout_3.addWidget(self.threshold1_lcd)
		self.threshold1_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
		self.threshold1_edit.setObjectName(_fromUtf8("threshold1_edit"))
		self.horizontalLayout_3.addWidget(self.threshold1_edit)
		self.threshold1_slider = QtGui.QSlider(self.verticalLayoutWidget)
		self.threshold1_slider.setMaximum(254)
		self.threshold1_slider.setOrientation(QtCore.Qt.Horizontal)
		self.threshold1_slider.setObjectName(_fromUtf8("threshold1_slider"))
		self.horizontalLayout_3.addWidget(self.threshold1_slider)
		self.verticalLayout_3.addLayout(self.horizontalLayout_3)
		self.horizontalLayout_4 = QtGui.QHBoxLayout()
		self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
		self.threshold2_lcd = QtGui.QLCDNumber(self.verticalLayoutWidget)
		self.threshold2_lcd.setObjectName(_fromUtf8("threshold2_lcd"))
		self.horizontalLayout_4.addWidget(self.threshold2_lcd)
		self.threshold2_edit = QtGui.QLineEdit(self.verticalLayoutWidget)
		self.threshold2_edit.setObjectName(_fromUtf8("threshold2_edit"))
		self.horizontalLayout_4.addWidget(self.threshold2_edit)
		self.threshold2_slider = QtGui.QSlider(self.verticalLayoutWidget)
		self.threshold2_slider.setMaximum(254)
		self.threshold2_slider.setOrientation(QtCore.Qt.Horizontal)
		self.threshold2_slider.setObjectName(_fromUtf8("threshold2_slider"))
		self.horizontalLayout_4.addWidget(self.threshold2_slider)
		self.verticalLayout_3.addLayout(self.horizontalLayout_4)
		self.horizontalLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
		self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(20, 20, 591, 41))
		self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
		self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
		self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
		self.file_edit = QtGui.QLineEdit(self.horizontalLayoutWidget_5)
		self.file_edit.setObjectName(_fromUtf8("file_edit"))
		self.horizontalLayout_5.addWidget(self.file_edit)
		self.file_button = QtGui.QPushButton(self.horizontalLayoutWidget_5)
		self.file_button.setObjectName(_fromUtf8("file_button"))
		self.horizontalLayout_5.addWidget(self.file_button)
		self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
		self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(530, 70, 91, 101))
		self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
		self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
		self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
		self.verticalLayout.setContentsMargins(-1, 1, -1, 1)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.exec_button = QtGui.QPushButton(self.verticalLayoutWidget_2)
		self.exec_button.setMinimumSize(QtCore.QSize(80, 60))
		self.exec_button.setObjectName(_fromUtf8("exec_button"))
		self.verticalLayout.addWidget(self.exec_button)
		self.cancel_button = QtGui.QPushButton(self.verticalLayoutWidget_2)
		self.cancel_button.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.cancel_button.setAcceptDrops(True)
		self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
		self.verticalLayout.addWidget(self.cancel_button)
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
		QtCore.QObject.connect(self.threshold1_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.threshold1_lcd.display)
		QtCore.QObject.connect(self.threshold2_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.threshold2_lcd.display)
		QtCore.QObject.connect(self.size_slider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.size_lcd.display)
		QtCore.QObject.connect(self.threshold1_edit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.threshold1_lcd.display)
		QtCore.QObject.connect(self.threshold2_edit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.threshold2_lcd.display)
		QtCore.QObject.connect(self.size_edit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.size_lcd.display)
		QtCore.QMetaObject.connectSlotsByName(Qt_CV_MainWindow)

	def retranslateUi(self, Qt_CV_MainWindow):
		Qt_CV_MainWindow.setWindowTitle(_translate("Qt_CV_MainWindow", "MainWindow", None))
		self.file_button.setText(_translate("Qt_CV_MainWindow", "File", None))
		self.exec_button.setText(_translate("Qt_CV_MainWindow", "Execute", None))
		self.cancel_button.setText(_translate("Qt_CV_MainWindow", "Cancel", None))
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

