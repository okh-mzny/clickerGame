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

#RaspberryPI
def raspberry_buy():
    if(mt.MathLogic.get_score()>=prices_dict["raspb_cost"]):
        mt.MathLogic.get_score()-prices_dict["raspb_cost"]
        prices_dict["raspb_cost"]=costincrement(prices_dict["raspb_cost"])
        return True
    else:
        return False
#Arduino    
def arduino_buy():
    if(mt.MathLogic.get_score()>=prices_dict["arduino_cost"]):
        mt.MathLogic.get_score()-prices_dict["arduino_cost"]
        prices_dict["arduino_cost"]=costincrement(prices_dict["arduino_cost"])
        return True
    else:
        return False
#CPU
def cpu_buy():
    if(mt.MathLogic.get_score()>=prices_dict["cpu_cost"]):
        mt.MathLogic.get_score()-prices_dict["cpu_cost"]
        prices_dict["cpu_cost"]=costincrement(prices_dict["cpu_cost"])
        return True
    else:
        return False    
#GPU
def gpu_buy():
    if(mt.MathLogic.get_score()>=prices_dict["gpu_cost"]):
        mt.MathLogic.get_score()-prices_dict["gpu_cost"]
        prices_dict["gpu_cost"]=costincrement(prices_dict["gpu_cost"])
        return True
    else:
        return False 
#Saugroboter
def saugroboter_buy():
    if(mt.MathLogic.get_score()>=prices_dict["saugroboter_cost"]):
        mt.MathLogic.get_score()-prices_dict["saugroboter_cost"]
        prices_dict["saugroboter_cost"]=costincrement(prices_dict["saugroboter_cost"])
        return True
    else:
        return False 
#MAC
def mac_buy():
    if(mt.MathLogic.get_score()>=prices_dict["mac_cost"]):
        mt.MathLogic.get_score()-prices_dict["mac_cost"]
        prices_dict["mac_cost"]=costincrement(prices_dict["mac_cost"])
        return True
    else:
        return False 
#Roboterarm
def roboteramrm_buy():
    if(mt.MathLogic.get_score()>=prices_dict["roboterarm_cost"]):
        mt.MathLogic.get_score()-prices_dict["roboterarm_cost"]
        prices_dict["roboterarm_cost"]=costincrement(prices_dict["roboterarm_cost"])
        return True
    else:
        return False