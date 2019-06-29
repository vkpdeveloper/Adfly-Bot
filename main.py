import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox, QMessageBox, QWidget, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
import pyautogui, time, subprocess
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
import re
import webbrowser

class App(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Adfly Bot ~ Vaibhav Pathak"
        self.left = 200
        self.top = 200
        self.height = 400
        self.width = 400
        self.iconName = "logo.png"
        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QIcon(self.iconName))
        self.setStyleSheet("background:white")
        # self.setAutoFillBackground(True)
        # p = self.palette()
        # p.setColor(self.backgroundRole(), Qt.white)
        # self.setPalette(p)
        App.setMinimumSize(self, QSize(400, 400))
        App.setMaximumSize(self, QSize(400, 400))
        self.uiComponet()
        self.show()

    def uiComponet(self):
        self.lbl1 = QLabel("Enter Your URL Here : ", self)
        self.lbl1.setFixedWidth(300)
        self.lbl1.setStyleSheet('color:#7b4397')
        self.lbl1.move(60, 40)
        self.url_box = QLineEdit(self)
        self.url_box.setFixedWidth(280)
        self.url_box.move(60, 70)
        self.url_box.setFocus()
        self.url_box.setStyleSheet('color:#7b4397')
        self.font = self.url_box.font()
        self.font.setPointSize(12)
        self.url_box.setFont(self.font)

        self.lbl2 = QLabel("Number of Clicks You Want : ", self)
        self.lbl2.move(60, 110)
        self.lbl2.setStyleSheet('color:#7b4397')
        self.lbl2.setFixedWidth(200)
        self.view_box = QLineEdit(self)
        self.view_box.setFixedWidth(280)
        self.view_box.setStyleSheet('color:#7b4397')
        self.view_box.move(60, 140)
        self.font = self.view_box.font()
        self.font.setPointSize(12)
        self.view_box.setFont(self.font)

        self.start_btn = QPushButton("Start", self)
        self.start_btn.setStyleSheet("background-color:#7b4397;color:white")
        self.start_btn.move(110, 200)
        self.start_btn.clicked.connect(self.onStart)

        self.htu_btn = QPushButton("How to Use ?", self)
        self.htu_btn.setStyleSheet("background-color:#dc2430;color:white")
        self.htu_btn.move(200, 200)
        self.htu_btn.clicked.connect(self.onHow)

        self.about_btn = QPushButton("About Developer", self)
        self.about_btn.setStyleSheet("background-color:#12c2e9;color:white")
        self.about_btn.move(160, 250)
        self.about_btn.clicked.connect(self.onAbout)

        self.aboutlbl = QLabel("Developed by Vaibhav Pathak", self)
        self.aboutlbl.move(2, 370)
        self.aboutlbl.setFixedWidth(500)

    def onAbout(self):
        webbrowser.open_new('http://vaibhavpathak.diagodevelopers.dx.am')

    def onStart(self):
        time.sleep(5)
        count = 1
        url = self.url_box.text()
        view_lbl = self.view_box.text()
        if url != "" and view_lbl != "":
            if re.search('http', url):
                    subprocess.Popen(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                    while count <= int(view_lbl):
                        if view_lbl != count:
                            if count >= 1:
                                if count == 1:
                                    time.sleep(5)
                                else:
                                    time.sleep(2)
                                pyautogui.click(375, 53, duration=1, button='left')
                                pyautogui.typewrite(url, interval=0.01)
                                pyautogui.press('enter')
                                time.sleep(10)
                                pyautogui.click(670, 287, duration=0.3, interval=0.3, button='left')
                                print("Waiting for 10 Seconds")
                                time.sleep(12)
                                pyautogui.rightClick(1241, 100, duration=1.0)
                                time.sleep(2)
                                pyautogui.click(1241, 110, interval=1.0, duration=1.0, button='left')
                                time.sleep(1)
                                pyautogui.click(370, 10, interval=0.1, duration=0.1, button='left')
                                time.sleep(8)
                                pyautogui.click(335, 162, interval=0.1, duration=0.1, button='left')
                                time.sleep(5)
                                count = count + 1
                                pyautogui.click(470, 14, duration=0.3, interval=0.3, button='left')

                        else:
                            get_msg =   QMessageBox.question(self, 'Task Successful',
                                                 "Task is Successfully Completed.",
                                                 QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)

            else:
                invalid_box = QMessageBox.question(self, 'Error Detected',
                                                 "URL is Not Valid !",
                                                 QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)

        else:
            error_box = QMessageBox.question(self, 'Blank Field Detected !',
                                            "Blank Fields are Detected in TextBoxes !",
                                            QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)

    def onHow(self):
        msg_box = QMessageBox.question(self, 'How to Use ?', "Note : If Your Start the Software to Do Clicking then You want to wait for that time (depends on your Clicks that you want) or You want to go to Task Manager and End Our Software Task.",
                                           QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
