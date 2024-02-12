import sys

from PyQt6 import QtWidgets, QtGui, uic

import gameLogic.main.items as itemDefinition

import gameLogic.main.math as gameMath
import gameLogic.shop.buyfuctions as gameBuyFunctions

cols = ['nameLabel',
        'oneGeneratingLabel',
        'costLabel',
        'buyButton',
        'totalOwnedLabel',
        'totalGeneratingLabel'
]


def init():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())


class MainWindow(QtWidgets.QMainWindow):
    gameMathObj = None
    gameShopObj = None

    shopItemWidgets = {}

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.gameMathObj = gameMath.MathLogic()
        self.gameShopObj = gameBuyFunctions.BuyFunctions(self.gameMathObj)

        uic.loadUi('gui/uic/gui.ui', self)
        self.pushButton.setIcon(QtGui.QIcon('gui/res/pushBtn.png'))

        for item in itemDefinition.items:
            newRowCount = self.shopTable.rowCount()
            self.shopItemWidgets[item['id']] = {
                'nameLabel': QtWidgets.QLabel(),
                'oneGeneratingLabel': QtWidgets.QLabel(),
                'costLabel': QtWidgets.QLabel(),
                'buyButton': QtWidgets.QPushButton("Buy"),
                'totalOwnedLabel': QtWidgets.QLabel(),
                'totalGeneratingLabel': QtWidgets.QLabel()
            }
            self.shopTable.insertRow(newRowCount)
            for col, col_name in enumerate(cols):
                if col_name is not None:
                    self.shopTable.setCellWidget(newRowCount, col, self.shopItemWidgets[item['id']][col_name])
            self.shopTable.cellWidget(newRowCount, cols.index('nameLabel')).setText(item['nameLabel'])
            self.shopTable.cellWidget(newRowCount, cols.index('oneGeneratingLabel')).setText(f'{item['power']}')
            self.shopTable.cellWidget(newRowCount, cols.index('costLabel')).setText(f'{item['cost']}')
            self.shopTable.cellWidget(newRowCount, cols.index('buyButton')).clicked.connect(self.clickHandler)

    def clickHandler(self):
        item_id = ""
        for item in itemDefinition.items:
            if self.sender() is self.shopItemWidgets[item['id']]['buyButton']:
                item_id = item['id']
                break
        print(item_id)
