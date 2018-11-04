#!/usr/bin/python3
# -*- coding: utf-8 -*-

# source http://zetcode.com/gui/pyqt5/menustoolbars/

import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context menu')
        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()
        elif action == opnAct:
            print("OPEN")
        elif action == newAct:
            print("NEW")
        else:
            print("hoooee")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
