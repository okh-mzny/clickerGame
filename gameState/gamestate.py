from PyQt6.QtCore import QSettings, QTimer
import gameState.items as itemDefinition


class GameState:
    # QSettings object that stores the game state in the OS user profile
    settings = QSettings(QSettings.Format.IniFormat, QSettings.Scope.UserScope, "ByteDashOrg", "ByteDash")

    autosaveTimer = QTimer()
    itemTable = {}

    score = 0

    def saveState(self):
        self.settings.setValue("score", self.score)
        for item_id, item in self.itemTable.items():
            self.settings.setValue(f"items/{item_id}/cost", item["cost"])
            self.settings.setValue(f"items/{item_id}/ownedCount", item["ownedCount"])
        self.settings.sync()

    def __init__(self):
        # Initialize itemTable as an id-itemData dictionary
        for item in itemDefinition.items:
            self.itemTable[item["id"]] = item.copy()

        # decide if this is a clean startup or there is existing data from a previous run
        if self.settings.allKeys():
            # we load in all data from the preference file
            self.score = int(self.settings.value("score"))
            for item_id, item in self.itemTable.items():
                item["cost"] = int(self.settings.value(f"items/{item_id}/cost"))
                item["ownedCount"] = int(self.settings.value(f"items/{item_id}/ownedCount"))

        else:
            # we need to initialize data for a new game from the item definition template
            # leave the itemTable as is (populated freshly from itemDefinitions)
            for item_id, item in self.itemTable.items():
                # Player does not own anything in a new game
                item["ownedCount"] = 0
        self.autosaveTimer.start(600000)  # autosave every 10 minutes
        self.autosaveTimer.timeout.connect(self.saveState)

