import math

import gameState.items as itemDefinition
from gameState.gamestate import GameState


class BuyFunctions:

    gameState = None

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def buy(self, item_id):
        # get item cost to use
        item_cost = self.gameState.itemTable[item_id]["cost"]
        # check if player can afford to buy item
        if self.gameState.score >= item_cost:
            # deduct the cost
            self.gameState.score -= item_cost
            # calculate the new cost of the item
            newCost = math.ceil(self.gameState.itemTable[item_id]["cost"] * self.gameState.itemTable[item_id]["costmod"])
            # set new cost of the item
            self.gameState.itemTable[item_id]["cost"] = newCost
            # player now owns one more of the item
            self.gameState.itemTable[item_id]["ownedCount"] += 1
            # signify successful purchase
            return True
        else:
            # can"t afford item
            return False

    def buy_upgrade(self, upgrade_id):
        #get upgrade
        upgrade = self.gameState.upgradeTable[upgrade_id]
        upgrade_cost = upgrade["cost"]
        fromid = upgrade["fromid"]
        fromitem = self.gameState.itemTable[fromid]
        toid = upgrade["toid"]
        toitem = self.gameState.itemTable[toid]
        # check if player can afford to buy upgrade
        if fromitem["ownedCount"] >= upgrade_cost:
            # deduct the cost from fromitem
            fromitem["ownedCount"] -= upgrade_cost
            # reset cost of fromitem
            fromitem["cost"] = int(fromitem["cost"] / math.pow(fromitem["costmod"]),upgrade_cost)
            # Add effect to toitem
            toitem["cost"] = int(toitem["cost"]*upgrade["redcost"])
            toitem["power"] += int(toitem["power"]*upgrade["powmod"])
            # Change state of upgrade
            upgrade["cost"] = int(upgrade_cost*upgrade["costmod"])
            self.gameState.upgradeTable[upgrade_id] = upgrade
            self.gameState.itemTable[toid] = toitem
            self.gameState.itemTable[fromid] = fromitem
            return True
        else:
            # can't afford upgrade
            return False