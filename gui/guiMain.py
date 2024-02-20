import math
import sys

from PyQt6 import QtWidgets, QtGui, QtCore, uic

from gameState.gamestate import GameState

import gameLogic.main.mathLogic as gameMath
import gameLogic.shop.buyfuctions as gameBuyFunctions

cols = ["nameLabel",
        "oneGeneratingLabel",
        "costLabel",
        "buyButton",
        "totalOwnedLabel",
        "totalGeneratingLabel"]


def init():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())


def prettyPrint(size_bytes):
    if size_bytes == 0:
        return "0 B"
    size_names = ("B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
    exp = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, exp)
    round_size = round(size_bytes / p, 2)
    return f"{round_size} {size_names[exp]}"


class MainWindow(QtWidgets.QMainWindow):
    gameState = GameState()
    gameMathObj = None
    gameShopObj = None

    shopItemWidgets = {}

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.gameMathObj = gameMath.MathLogic(self.gameState)
        self.gameShopObj = gameBuyFunctions.BuyFunctions(self.gameState)

        uic.loadUi("gui/uic/gui.ui", self)
        self.pushButton.setIcon(QtGui.QIcon("gui/res/pushBtn.png"))
        self.pushButton.clicked.connect(self.mainClickHandler)

        for item_id, item in self.gameState.itemTable.items():
            newRowCount = self.shopTable.rowCount()
            self.shopItemWidgets[item_id] = {
                "nameLabel": QtWidgets.QLabel(item["nameLabel"]),
                "oneGeneratingLabel": QtWidgets.QLabel(f'{prettyPrint(item["power"])}/s'),
                "costLabel": QtWidgets.QLabel(f'{prettyPrint(item["cost"])}'),
                "buyButton": QtWidgets.QPushButton("Buy"),
                "totalOwnedLabel": QtWidgets.QLabel(f'{item["ownedCount"]}'),
                "totalGeneratingLabel": QtWidgets.QLabel()
            }
            self.shopItemWidgets[item_id]["buyButton"].setAutoRepeat(True)
            self.shopItemWidgets[item_id]["buyButton"].setAutoRepeatInterval(1)

            self.shopTable.insertRow(newRowCount)
            for col, col_name in enumerate(cols):
                if col_name is not None:
                    self.shopTable.setCellWidget(newRowCount, col, self.shopItemWidgets[item_id][col_name])

            self.shopTable.cellWidget(newRowCount, cols.index("buyButton")).clicked.connect(self.buyClickHandler)

        self.gameTimer = QtCore.QTimer()
        self.gameTimer.timeout.connect(self.timerHandler)
        self.gameTimer.start(1000)
        self.refreshGuiValues()

    def closeEvent(self, a0):
        self.gameState.saveState()

    def refreshGuiValues(self):
        # update item lines
        for item_id, item in self.gameState.itemTable.items():
            self.shopItemWidgets[item_id]["costLabel"].setText(f'{prettyPrint(self.gameState.itemTable[item_id]["cost"])}')
            self.shopItemWidgets[item_id]["totalOwnedLabel"].setText(
                f'{self.gameState.itemTable[item_id]["ownedCount"]}')
            generation_sum = self.gameState.itemTable[item_id]["ownedCount"] * self.gameState.itemTable[item_id][
                "power"]
            self.shopItemWidgets[item_id]["totalGeneratingLabel"].setText(f"{prettyPrint(generation_sum)}/s")

        # update bps
        self.numBpsLabel.setText(f"Generating {prettyPrint(self.gameMathObj.total_gen())}/s")

    def mainClickHandler(self):
        self.gameState.score += math.ceil(0.01*self.gameMathObj.total_gen())
        self.numBytesLabel.setText(prettyPrint(self.gameState.score))

    def buyClickHandler(self):
        clicked_item_id = ""
        for item_id, item in self.gameState.itemTable.items():
            if self.sender() is self.shopItemWidgets[item_id]["buyButton"]:
                clicked_item_id = item_id
                break
        if clicked_item_id:
            buy_success = self.gameShopObj.buy(clicked_item_id)
            if buy_success:
                self.refreshGuiValues()

    def timerHandler(self):
        self.gameMathObj.update()
        self.numBytesLabel.setText(prettyPrint(self.gameState.score))
