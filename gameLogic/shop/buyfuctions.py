import gameLogic.main.math as mt
import items 

#Prices
prices_dict={
    "tasch_cost":10,
    "raspb_cost":10,
    "arduino_cost":10,
    "cpu_cost":10,
    "gpu_cost":10,
    "saugroboter_cost":10,
    "mac_cost":10,
    "roboterarm_cost":10
}


#General
def costincrement(cost):
    return cost+1

def costred(cost,costmod):
    cost=cost-cost*costmod
#Taschenrechner
def buy(item):
    if(mt.MathLogic.get_score()>=prices_dict["tasch_cost"]):
        mt.MathLogic.get_score()-prices_dict["tasch_cost"]
        prices_dict["tasch_cost"]=costincrement(prices_dict["tasch_cost"])
        return True
    else:
        return False
