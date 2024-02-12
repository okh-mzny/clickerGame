import sys

from PyQt6 import QtWidgets, QtGui, uic

import gameLogic.main.items as itemDefinition

cols = [None, 'nameLabel', 'oneGeneratingLabel', 'costLabel', 'buyButton', 'totalOwnedLabel', 'totalGeneratingLabel']


def init():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())


class MainWindow(QtWidgets.QMainWindow):
    shopItemWidgets = {}

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('gui/uic/gui.ui', self)
        self.pushButton.setIcon(QtGui.QIcon('gui/res/pushBtn.png'))

        for item in itemDefinition.items:
            newRowCount = self.shopTable.rowCount()
            self.shopItemWidgets[item['id']] = {
                'nameLabel': QtWidgets.QLabel(),
                'oneGeneratingLabel': QtWidgets.QLabel(),
                'costLabel': QtWidgets.QLabel(),
                'buyButton': QtWidgets.QPushButton(),
                'totalOwnedLabel': QtWidgets.QLabel(),
                'totalGeneratingLabel': QtWidgets.QLabel()
            }
            self.shopTable.insertRow(newRowCount)
            for col, col_name in enumerate(cols):
                if col_name is not None:
                    self.shopTable.setCellWidget(newRowCount, col, self.shopItemWidgets[item['id']][col_name])
