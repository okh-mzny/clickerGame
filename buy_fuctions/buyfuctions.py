#Prices
score = 19
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
    if(score>=tasch_cost):
        score-tasch_cost
        tasch_cost=costincrement(tasch_cost)
        return True
    else:
        return False

#RaspberryPI
def raspberry_buy():
    if(score>=raspb_cost):
        score-raspb_cost
        raspb_cost=costincrement(raspb_cost)
        return True
    else:
        return False
#Arduino    
def arduino_buy():
    if(score>=arduino_cos):
        score-arduino_cos
        arduino_cos=costincrement(arduino_cos)
        return True
    else:
        return False
#CPU
def cpu_buy():
    if(score>=cpu_cos):
        score-cpu_cos
        cpu_cos=costincrement(cpu_cos)
        return True
    else:
        return False    
#GPU
def gpu_buy():
    if(score>=gpu_cos):
        score-gpu_cos
        gpu_cos=costincrement(gpu_cos)
        return True
    else:
        return False 
#Saugroboter
def saugroboter_buy():
    if(score>=saugroboter_cos):
        score-saugroboter_cos
        saugroboter_cos=costincrement(saugroboter_cos)
        return True
    else:
        return False 
#MAC
def mac_buy():
    if(score>=mac_cos):
        score-mac_cos
        mac_cos=costincrement(mac_cos)
        return True
    else:
        return False 
#Roboterarm
def roboteramrm_buy():
    if(score>=roboterarm_cos):
        score-roboterarm_cos
        roboterarm_cos=costincrement(roboterarm_cos)
        return True
    else:
        return False