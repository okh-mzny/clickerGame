from PyQt6.QtCore import QSettings, QTimer
import gameState.items as itemDefinition
import gameState.upgrades as upgradeDefinition


class GameState:
    # QSettings object that stores the game state in the OS user profile
    settings = QSettings(QSettings.Format.IniFormat, QSettings.Scope.UserScope, "ByteDashOrg", "ByteDash")

    autosaveTimer = QTimer()
    itemTable = {}
    upgradeTable = {}

    score = 0

    # reset all values and sync reset values to disk
    def resetState(self):
        self.settings.setValue("score", 0)
        for item in itemDefinition.items:
            self.itemTable[item["id"]] = item.copy()
        for item_id, item in self.itemTable.items():
            self.settings.setValue(f"items/{item_id}/cost", item["cost"])
            self.settings.setValue(f"items/{item_id}/ownedCount", 0)
            self.settings.setValue(f"items/{item_id}/power", item["power"])
        for upgrade in upgradeDefinition.upgrades:
            self.upgradeTable[upgrade["id"]] = upgrade.copy()
        for upgrade_id, upgrade in self.upgradeTable.items():
            self.settings.setValue(f"upgrades/{upgrade_id}/cost", upgrade["cost"])
        self.settings.sync()
        self.initialize_Tables()

    def saveState(self):
        # loop over every existing data point and save them to QSettings
        self.settings.setValue("score", self.score)
        for item_id, item in self.itemTable.items():
            self.settings.setValue(f"items/{item_id}/cost", item["cost"])
            self.settings.setValue(f"items/{item_id}/ownedCount", item["ownedCount"])
            self.settings.setValue(f"items/{item_id}/power", item["power"])
        for upgrade_id, upgrade in self.upgradeTable.items():
            self.settings.setValue(f"upgrades/{upgrade_id}/cost", upgrade["cost"])
        # Sync to disk
        self.settings.sync()

    def __init__(self):

        self.initialize_Tables()

        self.autosaveTimer.start(600000)  # autosave every 10 minutes
        self.autosaveTimer.timeout.connect(self.saveState)

    def initialize_Tables(self):
        # Initialize itemTable as an id-itemData dictionary
        for item in itemDefinition.items:
            self.itemTable[item["id"]] = item.copy()

        # Initialize upgradeTable as an id-upgradeData dictionary
        for upgrade in upgradeDefinition.upgrades:
            self.upgradeTable[upgrade["id"]] = upgrade.copy()

        # decide if this is a clean startup or there is existing data from a previous run
        if self.settings.allKeys():
            # we load in all data from the preference file
            self.score = int(self.settings.value("score"))
            for item_id, item in self.itemTable.items():
                item["cost"] = int(self.settings.value(f"items/{item_id}/cost"))
                item["ownedCount"] = int(self.settings.value(f"items/{item_id}/ownedCount"))
                item["power"] = int(self.settings.value(f"items/{item_id}/power"))

            for upgrade_id, upgrade in self.upgradeTable.items():
                upgrade["cost"] = int(self.settings.value(f"upgrades/{upgrade_id}/cost"))

        else:
            # we need to initialize data for a new game from the item definition template
            # leave the itemTable as is (populated freshly from itemDefinitions)
            for item_id, item in self.itemTable.items():
                # Player does not own anything in a new game
                item["ownedCount"] = 0
