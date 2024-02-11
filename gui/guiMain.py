import sys
from pathlib import Path

from PyQt6 import QtWidgets, QtGui, uic

from dataclasses import dataclass


def init():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('gui/uic/gui.ui', self)
        self.pushButton.setIcon(QtGui.QIcon('gui/res/pushBtn.png'))
