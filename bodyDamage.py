# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bodyDamage.ui'
#
# Created: Wed May  8 20:08:56 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(670, 712)
        MainWindow.setMinimumSize(QtCore.QSize(670, 712))
        MainWindow.setMaximumSize(QtCore.QSize(670, 712))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 80, 381, 401))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("dudeVinci.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(300, 440, 16, 61))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(360, 440, 16, 61))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(310, 60, 20, 91))
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(110, 360, 141, 21))
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(397, 340, 151, 21))
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(440, 150, 118, 21))
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(80, 160, 121, 21))
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(150, 230, 181, 21))
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.line_9 = QtGui.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(150, 280, 171, 21))
        self.line_9.setLineWidth(2)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.nutHead = QtGui.QSpinBox(self.centralwidget)
        self.nutHead.setGeometry(QtCore.QRect(270, 40, 60, 27))
        self.nutHead.setMaximum(100)
        self.nutHead.setSingleStep(5)
        self.nutHead.setProperty("value", 100)
        self.nutHead.setObjectName(_fromUtf8("nutHead"))
        self.nutRhand = QtGui.QSpinBox(self.centralwidget)
        self.nutRhand.setGeometry(QtCore.QRect(30, 160, 60, 27))
        self.nutRhand.setMaximum(100)
        self.nutRhand.setSingleStep(5)
        self.nutRhand.setProperty("value", 100)
        self.nutRhand.setObjectName(_fromUtf8("nutRhand"))
        self.nutRleg = QtGui.QSpinBox(self.centralwidget)
        self.nutRleg.setGeometry(QtCore.QRect(60, 360, 60, 27))
        self.nutRleg.setMaximum(100)
        self.nutRleg.setSingleStep(5)
        self.nutRleg.setProperty("value", 100)
        self.nutRleg.setObjectName(_fromUtf8("nutRleg"))
        self.nutLleg = QtGui.QSpinBox(self.centralwidget)
        self.nutLleg.setGeometry(QtCore.QRect(540, 340, 60, 27))
        self.nutLleg.setMaximum(100)
        self.nutLleg.setSingleStep(5)
        self.nutLleg.setProperty("value", 100)
        self.nutLleg.setObjectName(_fromUtf8("nutLleg"))
        self.nutLhand = QtGui.QSpinBox(self.centralwidget)
        self.nutLhand.setGeometry(QtCore.QRect(540, 150, 60, 27))
        self.nutLhand.setMaximum(100)
        self.nutLhand.setSingleStep(5)
        self.nutLhand.setProperty("value", 100)
        self.nutLhand.setObjectName(_fromUtf8("nutLhand"))
        self.nutLbody = QtGui.QSpinBox(self.centralwidget)
        self.nutLbody.setGeometry(QtCore.QRect(100, 280, 60, 27))
        self.nutLbody.setMaximum(100)
        self.nutLbody.setSingleStep(5)
        self.nutLbody.setProperty("value", 100)
        self.nutLbody.setObjectName(_fromUtf8("nutLbody"))
        self.nutUbody = QtGui.QSpinBox(self.centralwidget)
        self.nutUbody.setGeometry(QtCore.QRect(100, 230, 60, 27))
        self.nutUbody.setMaximum(100)
        self.nutUbody.setSingleStep(5)
        self.nutUbody.setProperty("value", 100)
        self.nutUbody.setObjectName(_fromUtf8("nutUbody"))
        self.nutRfeet = QtGui.QSpinBox(self.centralwidget)
        self.nutRfeet.setGeometry(QtCore.QRect(260, 490, 60, 27))
        self.nutRfeet.setMaximum(100)
        self.nutRfeet.setSingleStep(5)
        self.nutRfeet.setProperty("value", 100)
        self.nutRfeet.setObjectName(_fromUtf8("nutRfeet"))
        self.nutLfeet = QtGui.QSpinBox(self.centralwidget)
        self.nutLfeet.setGeometry(QtCore.QRect(320, 490, 60, 27))
        self.nutLfeet.setMaximum(100)
        self.nutLfeet.setSingleStep(5)
        self.nutLfeet.setProperty("value", 100)
        self.nutLfeet.setObjectName(_fromUtf8("nutLfeet"))
        self.txtReport = QtGui.QPlainTextEdit(self.centralwidget)
        self.txtReport.setGeometry(QtCore.QRect(130, 550, 381, 111))
        self.txtReport.setObjectName(_fromUtf8("txtReport"))
        self.chkArrow = QtGui.QCheckBox(self.centralwidget)
        self.chkArrow.setGeometry(QtCore.QRect(130, 520, 211, 22))
        self.chkArrow.setObjectName(_fromUtf8("chkArrow"))
        self.pgbHP = QtGui.QProgressBar(self.centralwidget)
        self.pgbHP.setGeometry(QtCore.QRect(140, 10, 381, 21))
        self.pgbHP.setProperty("value", 100)
        self.pgbHP.setObjectName(_fromUtf8("pgbHP"))
        self.line_10 = QtGui.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(230, 60, 20, 121))
        self.line_10.setLineWidth(2)
        self.line_10.setFrameShape(QtGui.QFrame.VLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.line_11 = QtGui.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(380, 60, 20, 121))
        self.line_11.setLineWidth(2)
        self.line_11.setFrameShape(QtGui.QFrame.VLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.line_12 = QtGui.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(210, 50, 31, 21))
        self.line_12.setLineWidth(2)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.line_13 = QtGui.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(390, 50, 31, 21))
        self.line_13.setLineWidth(2)
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.nutRarm = QtGui.QSpinBox(self.centralwidget)
        self.nutRarm.setGeometry(QtCore.QRect(150, 50, 60, 27))
        self.nutRarm.setMaximum(100)
        self.nutRarm.setSingleStep(5)
        self.nutRarm.setProperty("value", 100)
        self.nutRarm.setObjectName(_fromUtf8("nutRarm"))
        self.nutLarm = QtGui.QSpinBox(self.centralwidget)
        self.nutLarm.setGeometry(QtCore.QRect(420, 50, 60, 27))
        self.nutLarm.setMaximum(100)
        self.nutLarm.setSingleStep(5)
        self.nutLarm.setProperty("value", 100)
        self.nutLarm.setObjectName(_fromUtf8("nutLarm"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.nutHead, self.nutRarm)
        MainWindow.setTabOrder(self.nutRarm, self.nutLarm)
        MainWindow.setTabOrder(self.nutLarm, self.nutRhand)
        MainWindow.setTabOrder(self.nutRhand, self.nutLhand)
        MainWindow.setTabOrder(self.nutLhand, self.nutUbody)
        MainWindow.setTabOrder(self.nutUbody, self.nutLbody)
        MainWindow.setTabOrder(self.nutLbody, self.nutRleg)
        MainWindow.setTabOrder(self.nutRleg, self.nutLleg)
        MainWindow.setTabOrder(self.nutLleg, self.nutRfeet)
        MainWindow.setTabOrder(self.nutRfeet, self.nutLfeet)
        MainWindow.setTabOrder(self.nutLfeet, self.chkArrow)
        MainWindow.setTabOrder(self.chkArrow, self.txtReport)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Body Damage Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.chkArrow.setText(QtGui.QApplication.translate("MainWindow", "Took an Arrow in the Knee", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

