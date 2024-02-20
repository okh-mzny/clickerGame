from gameState.gamestate import GameState


class MathLogic:

    gameState = None

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def update(self):
        # calculate total generation of all items
        item_generation_sum = self.total_gen()
        # add that to score
        self.gameState.score += item_generation_sum

    def total_gen(self):
        # enumerate combined generation of all items
        item_generation_sum = 0
        for item_id, item in self.gameState.itemTable.items():
            item_generation_sum += item["ownedCount"] * item["power"]
        return item_generation_sum