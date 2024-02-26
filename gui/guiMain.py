# python core
import math
import sys

# PyQt6
from PyQt6 import QtWidgets, QtGui, QtCore, uic

# Dialog code
import gui.dialogs as dialogs

# Game logic
from gameState.gamestate import GameState
import gameLogic.main.mathLogic as gameMath
import gameLogic.shop.buyfuctions as gameBuyFunctions

# Column ids by index
cols = ["nameLabel",
        "oneGeneratingLabel",
        "costLabel",
        "buyButton",
        "totalOwnedLabel",
        "totalGeneratingLabel"]


# We start here
def init():
    # Define a QApplication
    app = QtWidgets.QApplication(sys.argv)
    # The entire game is a QMainWindow
    mainWindow = MainWindow()
    # Show the Window, this enters an event loop and only returns if the window is closed
    mainWindow.show()
    # On normal close the show() returns and we safely exit the application
    sys.exit(app.exec())


# This function takes a value in bytes and returns it formatted with a binary prefix as defined by IEC
def prettyPrint(size_bytes):
    # The math below fails at 0, so we just return a hardcoded string
    if size_bytes == 0:
        return "0 B"
    # Indexed tuple of binary prefices, the appropriate one is calculated below
    size_names = ("B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
    exp = int(math.floor(math.log(size_bytes, 1024)))
    if exp < len(size_names):
        p = math.pow(1024, exp)
        round_size = round(size_bytes / p, 2)
        return f"{round_size} {size_names[exp]}"
    else:
        p = math.pow(1024, len(size_names) - 1)
        round_size = round(size_bytes / p, 2)
        exp = int(math.floor(math.log(round_size, 10)))
        final_size = round(round_size / math.pow(10, exp), 2)
        return f"{final_size}e{exp} {size_names[len(size_names) - 1]}"


class MainWindow(QtWidgets.QMainWindow):
    # MainWindow always starts out with a Gamestate object and later creates gameMath and gameShop with the gameState
    gameState = GameState()
    gameMathObj = None
    gameShopObj = None

    # Dicts containing dynamic widgets not defined by the UI file
    shopItemWidgets = {}
    upgradeItemWidgets = {}

    def __init__(self, *args, obj=None, **kwargs):
        # Initialize QMainWindow super, neccessary for Qt
        super(MainWindow, self).__init__(*args, **kwargs)

        # create the two logic objects, giving both a pointer to gameState to work on
        self.gameMathObj = gameMath.MathLogic(self.gameState)
        self.gameShopObj = gameBuyFunctions.BuyFunctions(self.gameState)

        # Load the UI structure as defined in a ui file from Qt Designer
        uic.loadUi("gui/uic/gui.ui", self)
        # Define the Icon for the main button manually, as Qt Designer uses a different resource reference model
        self.pushButton.setIcon(QtGui.QIcon("gui/res/pushBtn.png"))

        # Connect click handlers for the main buttons
        self.pushButton.clicked.connect(self.mainClickHandler)
        self.actionReset.triggered.connect(self.resetClickHandler)

        # Populate table with items defined in the gameState obejcts
        for item_id, item in self.gameState.itemTable.items():
            newRowCount = self.shopTable.rowCount()
            # create all elements in the row in the dict
            self.shopItemWidgets[item_id] = {
                "nameLabel": QtWidgets.QLabel(item["nameLabel"]),
                "oneGeneratingLabel": QtWidgets.QLabel(f'{prettyPrint(item["power"])}/s'),
                "costLabel": QtWidgets.QLabel(f'{prettyPrint(item["cost"])}'),
                "buyButton": QtWidgets.QPushButton("Buy"),
                "totalOwnedLabel": QtWidgets.QLabel(f'{item["ownedCount"]}'),
                "totalGeneratingLabel": QtWidgets.QLabel()
            }
            # set buy button to auto click on hold
            self.shopItemWidgets[item_id]["buyButton"].setAutoRepeat(True)
            self.shopItemWidgets[item_id]["buyButton"].setAutoRepeatInterval(1)

            # add the row and populate it with the items
            self.shopTable.insertRow(newRowCount)
            for col, col_name in enumerate(cols):
                if col_name is not None:
                    self.shopTable.setCellWidget(newRowCount, col, self.shopItemWidgets[item_id][col_name])
            # connect clickHandler to buy button
            self.shopTable.cellWidget(newRowCount, cols.index("buyButton")).clicked.connect(self.buyClickHandler)

        # Populate upgrade table, above comments apply
        for upgrade_id, upgrade in self.gameState.upgradeTable.items():
            newRowCount = self.upgradeTable.rowCount()
            self.upgradeItemWidgets[upgrade_id] = {
                "upgradeButton": QtWidgets.QPushButton(
                    f"{upgrade['nameLabel']} \nCost: {upgrade['cost']} {upgrade['costType']}")
            }

            self.upgradeItemWidgets[upgrade_id]["upgradeButton"].setAutoRepeat(True)
            self.upgradeItemWidgets[upgrade_id]["upgradeButton"].setAutoRepeatInterval(1)

            self.upgradeTable.insertRow(newRowCount)
            self.upgradeTable.setCellWidget(newRowCount, 0, self.upgradeItemWidgets[upgrade_id]["upgradeButton"])
            self.upgradeTable.cellWidget(newRowCount, 0).clicked.connect(self.upgradeClickHandler)

        # Create timer that fires every second to apply generation and refresh values
        self.gameTimer = QtCore.QTimer()
        self.gameTimer.timeout.connect(self.timerHandler)
        self.gameTimer.start(1000)
        self.refreshGuiValues()

    # save on program close
    def closeEvent(self, a0):
        self.gameState.saveState()

    # Ask for confirmation if reset button is clicked and reset if yes is answered
    def resetClickHandler(self):
        res = dialogs.showConfirmation("Zurücksetzen", "Soll das Spiel wirklich zurückgesetzt werden?")
        if res == QtWidgets.QMessageBox.StandardButton.Yes:
            self.gameState.resetState()
            self.refreshGuiValues()

    def refreshGuiValues(self):
        # update item lines
        for item_id, item in self.gameState.itemTable.items():
            self.shopItemWidgets[item_id]["costLabel"].setText(
                f'{prettyPrint(self.gameState.itemTable[item_id]["cost"])}')
            self.shopItemWidgets[item_id]["totalOwnedLabel"].setText(
                f'{self.gameState.itemTable[item_id]["ownedCount"]}')
            generation_sum = self.gameState.itemTable[item_id]["ownedCount"] * self.gameState.itemTable[item_id][
                "power"]
            self.shopItemWidgets[item_id]["totalGeneratingLabel"].setText(f"{prettyPrint(generation_sum)}/s")
            self.shopItemWidgets[item_id]["oneGeneratingLabel"].setText(f'{prettyPrint(item["power"])}/s')
        for upgrade_id, upgrade in self.gameState.upgradeTable.items():
            self.upgradeItemWidgets[upgrade_id]["upgradeButton"].setText(
                f"{upgrade['nameLabel']} \nCost: {upgrade['cost']} {upgrade['costType']}")

        # update bps and score
        self.numBpsLabel.setText(f"Generating {prettyPrint(self.gameMathObj.total_gen())}/s")
        self.numBytesLabel.setText(prettyPrint(self.gameState.score))

    # On click of main button, add 1% of current generation per second to score
    def mainClickHandler(self):
        if self.gameMathObj.total_gen() > 0:
            self.gameState.score += math.ceil(0.01 * self.gameMathObj.total_gen())
        else:
            self.gameState.score += 1
        self.numBytesLabel.setText(prettyPrint(self.gameState.score))

    def buyClickHandler(self):
        clicked_item_id = ""
        # enumerate all buttons to find the one that was clicked
        for item_id, item in self.gameState.itemTable.items():
            if self.sender() is self.shopItemWidgets[item_id]["buyButton"]:
                clicked_item_id = item_id
                # break if the items is found
                break
        if clicked_item_id:
            buy_success = self.gameShopObj.buy(clicked_item_id)
            if buy_success:
                self.refreshGuiValues()

    def timerHandler(self):
        self.gameMathObj.update()
        self.numBytesLabel.setText(prettyPrint(self.gameState.score))

    # similar to buyClickHandler
    def upgradeClickHandler(self):
        clicked_upgrade_id = ""
        for upgrade_id, upgrade in self.gameState.upgradeTable.items():
            if self.sender() is self.upgradeItemWidgets[upgrade_id]["upgradeButton"]:
                clicked_upgrade_id = upgrade_id
                break
        if clicked_upgrade_id:
            buy_success = self.gameShopObj.buy_upgrade(clicked_upgrade_id)
            if buy_success:
                self.refreshGuiValues()
