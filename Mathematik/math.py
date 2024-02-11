import time

curr_score=0

Items=[]

Items.append({
    "Name": "Taschenrechner",
    "Number": 13,
    "Power": 10
})

Items.append({
    "Name": "RaspberryPi",
    "Number": 5,
    "Power": 20
})

Itemsdict={
    "Taschenrechner":{
        "Name": "Taschenrechner",
        "Number": 13,
        "Power": 10
    },
    "RaspberryPi":{
        "Name": "RaspberryPi",
        "Number": 5,
        "Power": 20
    }
}

def AddNumtoItem(Num,Itemname):
    for Name in Itemsdict:
        if(Name==Itemname):
            Itemsdict[Name]["Number"]+=Num

def AddPowtoItem(Pow,Itemname):
    for Name in Itemsdict:
        if(Name==Itemname):
            Itemsdict[Name]["Power"]+=Pow

def MultPowofItem(Mult,Itemname):
    for Name in Itemsdict:
        if(Name==Itemname):
            Itemsdict[Name]["Power"]=Itemsdict[Name]["Power"]*Mult

def get_score():
    return curr_score

def Add_toScore(Scoreadd):
    global curr_score
    curr_score+=Scoreadd

def increment():
    total_incr=0
    for Item in Itemsdict:
        total_incr+=Itemsdict[Item]["Number"]*Itemsdict[Item]["Power"]
    return total_incr

def calc_twolog(rest_score):
    if(rest_score>=2):
        twolog=calc_twolog(rest_score/2)+1
        return twolog
    else:
        return 0

def get_twolog():
    return twolog

def calc_tenlog(rest_score):
    if(rest_score>=10):
        tenlog=calc_tenlog(rest_score/10)+1
        return tenlog
    else:
        return 0

def get_tenlog():
    return tenlog

def pot2(exp):
    if(exp==0):
        return 1
    else:
        pot=1
        for i in range(exp):
            pot=pot*2
    return pot

def pot(exp):
    if(exp==0):
        return 1
    else:
        pot=1
        for i in range(exp):
            pot=pot*10
    return pot

if(__name__=="__main__"):
    #for item in Items:
    #    if(item["Name"]=="Taschenrechner"):
    #        print(Items[Items.index(item)])
    #        item["Number"]=item["Number"]+1
    #        print(Items[Items.index(item)])
    while True:
        twolog=calc_twolog(get_score())
        if(twolog<10):
            new_score=curr_score
            print("{:.2f}".format(curr_score)+"byte")
        elif(twolog<20):
            new_score=curr_score/pot2(10)
            print("{:.2f}".format(curr_score/pot2(10))+"kb")
        elif(twolog<30):
            new_score=curr_score/pot2(20)
            print("{:.2f}".format(curr_score/pot2(20))+"Mb")
        elif(twolog<40):
            new_score=curr_score/pot2(30)
            print("{:.2f}".format(curr_score/pot2(30))+"Gb")
        elif(twolog<50):
            new_score=curr_score/pot2(40)
            print("{:.2f}".format(curr_score/pot2(40))+"Tb")
        else:
            new_score=curr_score/pot2(40)
            tenlog=calc_tenlog(new_score)
            print("{:.2f}".format(new_score/pot(tenlog))+"e"+str(tenlog)+" Tb")
        Add_toScore(increment())
        AddNumtoItem(1,"Taschenrechner")
        AddPowtoItem(1,"RaspberryPi")
        MultPowofItem(1.01,"Taschenrechner")
        time.sleep(1)
