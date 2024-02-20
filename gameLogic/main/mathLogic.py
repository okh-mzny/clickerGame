import math
import time
import gameLogic.main.items as itemDefinition


class MathLogic:
    twolog = 0
    tenlog = 0

    curr_score = 0

    items_dict = {}

    def __init__(self):
        for item in itemDefinition.items:
            self.items_dict[item['id']] = {}
            self.items_dict[item['id']]['power'] = item['power']
            self.items_dict[item['id']]['number'] = 0

    def AddNumtoItem(self, Num, item_id):
        if item_id in self.items_dict.keys():
            self.items_dict[item_id]["number"] += Num

    def AddPowtoItem(self, Pow, item_id):
        if item_id in self.items_dict.keys():
            self.items_dict[item_id]["power"] += Pow

    def MultPowofItem(self, Mult, item_id):
        if item_id in self.items_dict.keys():
            self.items_dict[item_id]["power"] = self.items_dict[item_id]["power"] * Mult

    def get_score(self):
        return self.curr_score

    def Remove_fromScore(self, Scorerem):
        self.curr_score -= Scorerem

    def Add_toScore(self, Scoreadd):
        self.curr_score += Scoreadd

    def increment(self):
        total_incr = 0
        for Item in self.items_dict:
            total_incr += self.items_dict[Item]["number"] * self.items_dict[Item]["power"]
        return total_incr

    def calc_twolog(self, rest_score):
        if rest_score >= 2:
            self.twolog = self.calc_twolog(rest_score / 2) + 1
            return self.twolog
        else:
            return 0

    def get_twolog(self):
        return self.twolog

    def calc_tenlog(self, rest_score):
        if rest_score >= 10:
            tenlog = self.calc_tenlog(rest_score / 10) + 1
            return tenlog
        else:
            return 0

    def get_tenlog(self):
        return self.tenlog

    def pot2(self, exp):
        if exp == 0:
            return 1
        else:
            pot = 1
            for i in range(exp):
                pot = pot * 2
        return pot

    def pot(self, exp):
        if exp == 0:
            return 1
        else:
            pot = 1
            for i in range(exp):
                pot = pot * 10
        return pot

    def prettyPrint(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    def update(self):
        self.Add_toScore(self.increment())

