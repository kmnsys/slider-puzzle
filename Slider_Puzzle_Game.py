import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QHBoxLayout,\
                            QAction, qApp, QWidget, QMessageBox, QLabel,QPushButton
from PyQt5.QtGui import QDesktopServices, QFont
from PyQt5.QtCore import QUrl
import random

m1 = (0, 80)
m2 = (80, 0)
m3 = (160, 0)
m3_1 = (-160, 0)
m4 = (0, 160)
m4_1 = (0, -160)
m5 = (240, 0)
m5_1 = (-240, 0)
m6= (0, 240)
m6_1 = (0, -240)

coords = [(0, 0), (80, 0), (160, 0), (240, 0),
          (0, 80), (80, 80), (160, 80), (240, 80),
          (0, 160), (80, 160), (160, 160), (240, 160),
          (0, 240), (80, 240), (160, 240), (240, 240)]

rightOrder = [1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 0]

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.content = PlaceButton()
        self.setCentralWidget(self.content)

        self.initMW()

    def initMW(self):
        menubar = self.menuBar()
        file = menubar.addMenu("About")

        github = QAction("Github Codes", self)
        github.triggered.connect(self.openUrl)
        github.setStatusTip("Click To Connect Github and View The Codes")
        file.addAction(github)

        exitAct = QAction("Quit", self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip("Click to quit")
        exitAct.triggered.connect(qApp.quit)
        file.addAction(exitAct)

        self.statusBar()
        self.setStyleSheet("background-color: white")
        self.setGeometry(300, 250, 590, 375)
        self.setFixedSize(590, 375)
        self.setWindowTitle('Slider Puzzle | Selman Y.')
        self.show()

    def openUrl(self):
        url = QUrl("https://github.com/kmnsys/slider-puzzle")
        if not QDesktopServices.openUrl(url):
            QMessageBox.warning(self, 'Open Url', 'Could not Open Url')


class PlaceButton(QWidget):

    def __init__(self):
        super().__init__()

        self.clickCount = 0
        self.initPB()

    def initPB(self):
        self.font = QFont()
        self.font.setPointSize(19)
        hbox = QHBoxLayout()
        self.setLayout(hbox)
        self.label = QLabel()
        self.clickCountLabel = QLabel()
        hbox.addWidget(self.label)
        hbox.addWidget(self.clickCountLabel)
        self.clickCountLabel.setMaximumWidth(210)
        self.clickCountLabel.setFont(self.font)
        self.clickCountLabel.setStyleSheet("color: #585942")


        self.table()

    def table(self):
        self.one = ""
        self.two = ""
        self.three = ""
        self.four = ""
        self.five = ""
        self.six = ""
        self.seven = ""
        self.eight = ""
        self.nine = ""
        self.ten = ""
        self.eleven = ""
        self.twelve = ""
        self.thirteen = ""
        self.fourteen = ""
        self.fifteen = ""

        self.newl = [self.one, self.two, self.three, self.four, self.five,
                     self.six, self.seven, self.eight, self.nine, self.ten,
                     self.eleven, self.twelve, self.thirteen, self.fourteen,
                     self.fifteen]

        self.buttonsOrder = []

        self.places = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                       10, 11, 12, 13, 14, 15]

        random.shuffle(self.places)

        m = 0

        for i in self.places:
            self.newl[i - 1] = QPushButton(str(i), self.label)
            self.newl[i - 1].setStyleSheet("""background-color: #078ab2;
                                              color: white;
                                              border-style: outset;
                                              border-width: 4px;    
                                              border-color: beige 
                                              """)
            self.newl[i - 1].setFont(self.font)
            self.newl[i - 1].resize(77, 77)
            self.newl[i - 1].move(*coords[m])
            self.newl[i - 1].clicked.connect(self.moveButton)
            self.buttonsOrder.append(self.newl[i - 1])
            m = m + 1

        self.places.append(0)
        self.buttonsOrder.append(0)

    def moveButton(self):
        sender = self.sender()
        self.senderC = sender
        senderText = sender.text()

        self.emptyCooords = coords[self.places.index(0)]
        self.pressButtonCoords = (sender.x(), sender.y())

        diffCoords = (abs(self.emptyCooords[0] - self.pressButtonCoords[0]),
                      abs(self.emptyCooords[1] - self.pressButtonCoords[1]))

        diffTwoBlock = (self.emptyCooords[0] - self.pressButtonCoords[0],
                        self.emptyCooords[1] - self.pressButtonCoords[1])

        if diffCoords == m1 or diffCoords == m2:
            sender.move(*self.emptyCooords)
            self.organize(senderText, sender)

            self.emptyCooords = coords[self.places.index(0)]

            self.clickCounts()
            self.finishGame()

        elif diffTwoBlock == m3:
            senderButtonIndex = self.places.index(int(senderText))
            senderButtonRight = self.buttonsOrder[senderButtonIndex + 1]
            senderButtonRightText = senderButtonRight.text()

            senderButtonRight.move(*self.emptyCooords)
            self.organize(senderButtonRightText, senderButtonRight)

            self.emptyCooords = coords[self.places.index(0)]

            sender.move(*self.emptyCooords)
            self.organize(senderText, sender)

            self.clickCounts()
            self.finishGame()

        elif diffTwoBlock == m3_1:
            senderButtonIndex = self.places.index(int(senderText))
            senderButtonLeft = self.buttonsOrder[senderButtonIndex - 1]
            senderButtonLeftText = senderButtonLeft.text()

            senderButtonLeft.move(*self.emptyCooords)
            self.organize(senderButtonLeftText, senderButtonLeft)

            self.emptyCooords = coords[self.places.index(0)]

            sender.move(*self.emptyCooords)
            self.organize(senderText, sender)

            self.clickCounts()
            self.finishGame()

        elif diffTwoBlock == m4_1:
            senderButtonIndex = self.places.index(int(senderText))
            senderButtonUp = self.buttonsOrder[senderButtonIndex -4]
            senderButtonLeftText = senderButtonUp.text()

            senderButtonUp.move(*self.emptyCooords)
            self.organize(senderButtonLeftText, senderButtonUp)

            self.emptyCooords = coords[self.places.index(0)]

            sender.move(*self.emptyCooords)
            self.organize(senderText, sender)

            self.clickCounts()
            self.finishGame()

        elif diffTwoBlock == m4:
            senderButtonIndex = self.places.index(int(senderText))
            senderButtonDown = self.buttonsOrder[senderButtonIndex +4]
            senderButtonLeftText = senderButtonDown.text()

            senderButtonDown.move(*self.emptyCooords)
            self.organize(senderButtonLeftText, senderButtonDown)

            self.emptyCooords = coords[self.places.index(0)]

            sender.move(*self.emptyCooords)
            self.organize(senderText, sender)

            self.clickCounts()
            self.finishGame()

        elif diffTwoBlock == m5:
            senderButtonIndex = self.places.index(int(senderText))
            senderButtonRight = self.buttonsOrder[senderButtonIndex + 1]
            senderButtonRightText = senderButtonRight.text()

            senderButtonRightToRight = self.buttonsOrder[senderButtonIndex + 2]
            senderButtonRightToRightText = senderButtonRightToRight.text()

            senderButtonRightToRight.move(*self.emptyCooords)
            self.organize(senderButtonRightToRightText, senderButtonRightToRight)

            self.emptyCooords = coords[self.places.index(0)]

            senderButtonRight.move(*self.emptyCooords)
            self.organize(senderButtonRightText, senderButtonRight)

            self.emptyCooords = coords[self.places.index(0)]

            sender.move(*self.emptyCooords)
            self.organize(senderText, sender)

            self.clickCounts()
            self.finishGame()

        elif diffTwoBlock == m5_1:
            senderButtonIndex = self.places.index(int(senderText))
            senderButtonRight = self.buttonsOrder[senderButtonIndex - 1]
            senderButtonRightText = senderButtonRight.text()

            senderButtonRightToRight = self.buttonsOrder[senderButtonIndex - 2]
            senderButtonRightToRightText = senderButtonRightToRight.text()

            senderButtonRightToRight.move(*self.emptyCooords)
            self.organize(senderButtonRightToRightText, senderButtonRightToRight)

            self.emptyCooords = coords[self.places.index(0)]

            senderButtonRight.move(*self.emptyCooords)
            self.organize(senderButtonRightText, senderButtonRight)

            self.emptyCooords = coords[self.places.index(0)]

            sender.move(*self.emptyCooords)
            self.organize(senderText, sender)

            self.clickCounts()
            self.finishGame()

        elif diffTwoBlock == m6_1:
            senderButtonIndex = self.places.index(int(senderText))
            senderButtonUp = self.buttonsOrder[senderButtonIndex -4]
            senderButtonUpText = senderButtonUp.text()

            senderButtonUpToUp = self.buttonsOrder[senderButtonIndex -8]
            senderButtonUpToUpText = senderButtonUpToUp.text()

            senderButtonUpToUp.move(*self.emptyCooords)
            self.organize(senderButtonUpToUpText, senderButtonUpToUp)

            self.emptyCooords = coords[self.places.index(0)]

            senderButtonUp.move(*self.emptyCooords)
            self.organize(senderButtonUpText, senderButtonUp)

            self.emptyCooords = coords[self.places.index(0)]

            sender.move(*self.emptyCooords)
            self.organize(senderText, sender)

            self.clickCounts()
            self.finishGame()

        elif diffTwoBlock == m6:
            senderButtonIndex = self.places.index(int(senderText))
            senderButtonUp = self.buttonsOrder[senderButtonIndex +4]
            senderButtonUpText = senderButtonUp.text()

            senderButtonUpToUp = self.buttonsOrder[senderButtonIndex +8]
            senderButtonUpToUpText = senderButtonUpToUp.text()

            senderButtonUpToUp.move(*self.emptyCooords)
            self.organize(senderButtonUpToUpText, senderButtonUpToUp)

            self.emptyCooords = coords[self.places.index(0)]

            senderButtonUp.move(*self.emptyCooords)
            self.organize(senderButtonUpText, senderButtonUp)

            self.emptyCooords = coords[self.places.index(0)]

            sender.move(*self.emptyCooords)
            self.organize(senderText, sender)

            self.clickCounts()
            self.finishGame()


    def clickCounts(self):
        self.clickCount += 1
        self.clickCountLabel.setText("Click Count: " + str(self.clickCount))

    def organize(self, stext, sbutton):
        emptyBtnPlc, pressBtnPlc = self.places.index(0), self.places.index(int(stext))
        self.places[pressBtnPlc], self.places[emptyBtnPlc] = self.places[emptyBtnPlc], self.places[pressBtnPlc]

        emptyBtnPlc1, pressBtnPlc1 = self.buttonsOrder.index(0), self.buttonsOrder.index(sbutton)
        self.buttonsOrder[pressBtnPlc1], self.buttonsOrder[emptyBtnPlc1] = self.buttonsOrder[emptyBtnPlc1], \
                                                                           self.buttonsOrder[pressBtnPlc1]

    def finishGame(self):
        if self.places == rightOrder:
            self.clickCountLabel.setText("GAME OVER" + "\n\n" + "Click Count: " + str(self.clickCount))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pb = MainWindow()
    sys.exit(app.exec_())
