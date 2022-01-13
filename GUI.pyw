from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import os
import sys
import math
import keyboard
import psutil
import pyautogui
import time
import datetime
import random
import winshell
import os.path
import ctypes
import winsound

from random import randint
from time import sleep
from colorama import Fore, Style
from colorama import init
from playsound import playsound

def Mbox(title, text, style):
    winsound.MessageBeep()
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def check1():
    if os.path.isfile('scripts\launcher_config.txt'):
        print()
    else:
        Mbox('Error', "You didn't ran Setup.bat correctly, rerun it and complete instalation to proceed.",0)
        sys.exit()

def check2():
    with open('scripts\launcher_config.txt') as f:
        if 'stm' in f.read():
            webbrowser.open_new_tab(url1)
        else:
            with open('scripts\launcher_config.txt') as f:
                if 'upl' in f.read():
                    webbrowser.open_new_tab(url)
                else:
                    Mbox('Error', "You didn't ran Setup.bat correctly, rerun it and complete instalation to proceed.",0)
                    sys.exit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon("assets\\rainbowium.png"))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 261)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(484, 261))
        MainWindow.setMaximumSize(QtCore.QSize(484, 261))
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(150, 10, 101, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 40, 481, 191))
        self.textEdit.setObjectName("textEdit")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(270, 200, 231, 31))
        self.commandLinkButton.setObjectName("commandLinkButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 21))
        self.menubar.setObjectName("menubar")
        self.menuApplication = QtWidgets.QMenu(self.menubar)
        self.menuApplication.setObjectName("menuApplication")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuApplication.addAction(self.actionExit)
        self.menubar.addAction(self.menuApplication.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.textEdit.setDisabled(True)
        self.checkBox.clicked.connect(lambda: self.start_stop())
        self.checkBox_2.clicked.connect(lambda: self.mutesound())
        self.actionExit.triggered.connect(lambda: self.exit())
        self.commandLinkButton.clicked.connect(lambda: self.browser_open())

        if os.path.isfile("configs\\soundconfig.txt"):
            self.checkBox_2.setChecked(True)

    def start_stop(self):
        if self.checkBox.isChecked():
            if os.path.isfile("configs\\soundconfig.txt"):
                print("")
            else:
                try:
                    playsound("sound\\launch.mp3", False)
                except Exception:
                    pass
            
            try:
                os.startfile("R6Bot.py")
            except Exception:
                pass
        else:
            if os.path.isfile("configs\\soundconfig.txt"):
                print("")
            else:
                try:
                    playsound("sound\\delaunch.mp3", False)
                except Exception:
                    pass
            os.system("taskkill /f /im python.exe /t")
            os.system("taskkill /f /im py.exe /t")

    def mutesound(self):
        if os.path.isdir("configs"):
            print("")
        else:
            os.mkdir("configs")
        if self.checkBox_2.isChecked():
            try:
                playsound("sound\\enable.mp3", False)
            except Exception:
                pass
            f = open("configs\\soundconfig.txt", "w")
            f.write("Disabled")
            f.close() 
        else:
            try:
                playsound("sound\\disable.mp3", False)
            except Exception:
                pass

            try:
                os.remove("configs\\soundconfig.txt")
            except Exception:
                pass

    def browser_open(self):
        webbrowser.open_new("https://github.com/DuroDaCoder/Rainbowium")


    def exit(self):
        sys.exit()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rainbowium GUI"))
        self.checkBox.setText(_translate("MainWindow", "Rainbowium Start/Stop"))
        self.checkBox_2.setText(_translate("MainWindow", "Mute Sounds"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Help:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">To run Rainbowium script, just check: &quot;Rainbowium Start/Stop&quot;.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">To stop Rainbowium script, make sure you you uncheck: &quot;Rainbowium Start/Stop&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">To mute Sounds in Rainbowium script, check: &quot;Mute Sounds&quot; to mute sounds.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">To unmute Sounds, just uncheck: &quot;Mute Sounds&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">To exit GUI, click &quot;X&quot; located in top right, or &quot;Application&quot; button and &quot;Exit&quot;.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">                    </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">Copyright: DuroDaCoder</span></p></body></html>"))
        self.commandLinkButton.setText(_translate("MainWindow", "Visit Rainbowium GitHub"))
        self.menuApplication.setTitle(_translate("MainWindow", "Application"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    check1()
    check2()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
