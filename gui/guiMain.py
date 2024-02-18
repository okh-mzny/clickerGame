import sys

from PyQt6 import QtWidgets, QtGui, QtCore, uic

import gameLogic.main.items as itemDefinition

import gameLogic.main.mathLogic as gameMath
import gameLogic.shop.buyfuctions as gameBuyFunctions

cols = ['nameLabel',
        'oneGeneratingLabel',
        'costLabel',
        'buyButton',
        'totalOwnedLabel',
        'totalGeneratingLabel']


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
        self.pushButton.clicked.connect(self.mainClickHandler)

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
            self.shopTable.cellWidget(newRowCount, cols.index('oneGeneratingLabel')).setText(f'{item["power"]}')
            self.shopTable.cellWidget(newRowCount, cols.index('costLabel')).setText(f'{item["cost"]}')
            self.shopTable.cellWidget(newRowCount, cols.index('buyButton')).clicked.connect(self.buyClickHandler)

            self.gameTimer = QtCore.QTimer()
            self.gameTimer.timeout.connect(self.timerHandler)
            self.gameTimer.start(1000)
            self.updateTotalBps()
            

    def updatePrice(self,item_id):
        self.shopItemWidgets[item_id]['costLabel'].setText(f'{self.gameShopObj.prices_dict[item_id]}')

    def updateTotalBps(self):
        sum = 0
        for item in itemDefinition.items:
            item_id = item['id']
            sum += self.gameMathObj.items_dict[item_id]["number"] * self.gameMathObj.items_dict[item_id]["power"]
        self.numBpsLabel.setText(f"Generating {self.gameMathObj.prettyPrint(sum)}/s")

    def mainClickHandler(self):
        self.gameMathObj.Add_toScore(1)

    def buyClickHandler(self):
        item_id = ""
        for item in itemDefinition.items:
            if self.sender() is self.shopItemWidgets[item['id']]['buyButton']:
                item_id = item['id']
                break
        if item_id:
            buy_success = self.gameShopObj.buy(item_id)
            if buy_success:
                self.shopItemWidgets[item_id]['totalOwnedLabel'].setText(
                    f'{self.gameMathObj.items_dict[item_id]["number"]}')
                self.shopItemWidgets[item_id]['totalGeneratingLabel'].setText(
                    f'{self.gameMathObj.items_dict[item_id]["number"] * self.gameMathObj.items_dict[item_id]["power"]}')
                self.updateTotalBps()
                self.updatePrice(item_id)

    def timerHandler(self):
        self.gameMathObj.update()
        self.numBytesLabel.setText(self.gameMathObj.prettyPrint(self.gameMathObj.curr_score))
