import math

import gameState.items as itemDefinition
from gameState.gamestate import GameState


class BuyFunctions:

    gameState = None

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def buy(self, item_id):
        # get item cost to use
        item_cost = self.gameState.itemTable[item_id]['cost']
        # check if player can afford to buy item
        if self.gameState.score >= item_cost:
            # deduct the cost
            self.gameState.score -= item_cost
            # calculate the new cost of the item
            newCost = math.ceil(self.gameState.itemTable[item_id]['cost'] * self.gameState.itemTable[item_id]['costmod'])
            # set new cost of the item
            self.gameState.itemTable[item_id]['cost'] = newCost
            # player now owns one more of the item
            self.gameState.itemTable[item_id]['ownedCount'] += 1
            # signify successful purchase
            return True
        else:
            # can't afford item
            return False
