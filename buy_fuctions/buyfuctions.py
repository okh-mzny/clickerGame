import Mathematik.math as mt
import  pandas as pd
#Prices
tasch_cost=1
raspb_cost=2
arduino_cos=3
cpu_cos=4
gpu_cos=5
saugroboter_cos=6
mac_cos=7
roboterarm_cos=8


#General
def costincrement(cost):
    return cost+1

def costred(cost,costmod):
    cost=cost-cost*costmod

#Taschenrechner
def tasch_buy():
    if(mt.get_score>=tasch_cost):
        mt.get_score-tasch_cost
        tasch_cost=costincrement(tasch_cost)
        return True
    else:
        return False

#RaspberryPI
def raspberry_buy():
    if(mt.get_score>=raspb_cost):
        mt.get_score-raspb_cost
        raspb_cost=costincrement(raspb_cost)
        return True
    else:
        return False
#Arduino    
def arduino_buy():
    if(mt.get_score>=arduino_cos):
        mt.get_score-arduino_cos
        arduino_cos=costincrement(arduino_cos)
        return True
    else:
        return False
#CPU
def cpu_buy():
    if(mt.get_score>=cpu_cos):
        mt.get_score-cpu_cos
        cpu_cos=costincrement(cpu_cos)
        return True
    else:
        return False    
#GPU
def gpu_buy():
    if(mt.get_score>=gpu_cos):
        mt.get_score-gpu_cos
        gpu_cos=costincrement(gpu_cos)
        return True
    else:
        return False 
#Saugroboter
def saugroboter_buy():
    if(mt.get_score>=saugroboter_cos):
        mt.get_score-saugroboter_cos
        saugroboter_cos=costincrement(saugroboter_cos)
        return True
    else:
        return False 
#MAC
def mac_buy():
    if(mt.get_score>=mac_cos):
        mt.get_score-mac_cos
        mac_cos=costincrement(mac_cos)
        return True
    else:
        return False 
#Roboterarm
def roboteramrm_buy():
    if(mt.get_score>=roboterarm_cos):
        mt.get_score-roboterarm_cos
        roboterarm_cos=costincrement(roboterarm_cos)
        return True
    else:
        return False