import gameLogic.main.items as itemDefinition


class BuyFunctions:
    mtObject = None
    prices_dict = {}

    def __init__(self, mtObject):
        self.mtObject = mtObject
        for item in itemDefinition.items:
            self.prices_dict[item['id']] = item['cost']

    # General
    def costincrement(self, cost):
        return cost + 1

    def costred(self, cost, costmod):
        cost = cost - cost * costmod

    def buy(self, item_id):
        if self.mtObject.get_score() >= self.prices_dict[item_id]:
            self.mtObject.get_score() - self.prices_dict[item_id]
            self.prices_dict[item_id] = self.costincrement(self.prices_dict[item_id])
            return True
        else:
            return False
