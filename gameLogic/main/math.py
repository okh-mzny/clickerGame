import time

class MathLogic:

    curr_score=0

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

    def AddNumtoItem(self, Num,Itemname):
        for Name in self.Itemsdict:
            if(Name==Itemname):
                self.Itemsdict[Name]["Number"]+=Num

    def AddPowtoItem(self, Pow,Itemname):
        for Name in self.Itemsdict:
            if(Name==Itemname):
                self.Itemsdict[Name]["Power"]+=Pow

    def MultPowofItem(self, Mult,Itemname):
        for Name in self.Itemsdict:
            if(Name==Itemname):
                self.Itemsdict[Name]["Power"]=self.Itemsdict[Name]["Power"]*Mult

    def get_score(self):
        return curr_score

    def Add_toScore(self, Scoreadd):
        global curr_score
        curr_score+=Scoreadd

    def increment(self):
        total_incr=0
        for Item in self.Itemsdict:
            total_incr+=self.Itemsdict[Item]["Number"]*self.Itemsdict[Item]["Power"]
        return total_incr

    def calc_twolog(self, rest_score):
        if(rest_score>=2):
            twolog=self.calc_twolog(rest_score/2)+1
            return twolog
        else:
            return 0

    def get_twolog(self):
        return twolog

    def calc_tenlog(self, rest_score):
        if(rest_score>=10):
            tenlog=self.calc_tenlog(rest_score/10)+1
            return tenlog
        else:
            return 0

    def get_tenlog(self):
        return tenlog

    def pot2(self, exp):
        if(exp==0):
            return 1
        else:
            pot=1
            for i in range(exp):
                pot=pot*2
        return pot

    def pot(self, exp):
        if(exp==0):
            return 1
        else:
            pot=1
            for i in range(exp):
                pot=pot*10
        return pot

if(__name__=="__main__"):
    mathlogic = MathLogic()
    while True:
        twolog=mathlogic.calc_twolog(mathlogic.get_score())
        if(twolog<10):
            new_score=mathlogic.curr_score
            print("{:.2f}".format(mathlogic.curr_score)+"Byte")
        elif(twolog<20):
            new_score=mathlogic.curr_score/mathlogic.pot2(10)
            print("{:.2f}".format(mathlogic.curr_score/mathlogic.pot2(10))+"kB")
        elif(twolog<30):
            new_score=mathlogic.curr_score/mathlogic.pot2(20)
            print("{:.2f}".format(mathlogic.curr_score/mathlogic.pot2(20))+"MB")
        elif(twolog<40):
            new_score=mathlogic.curr_score/mathlogic.pot2(30)
            print("{:.2f}".format(mathlogic.curr_score/mathlogic.pot2(30))+"GB")
        elif(twolog<50):
            new_score=mathlogic.curr_score/mathlogic.pot2(40)
            print("{:.2f}".format(mathlogic.curr_score/mathlogic.pot2(40))+"TB")
        else:
            new_score=mathlogic.curr_score/mathlogic.pot2(40)
            tenlog=mathlogic.calc_tenlog(new_score)
            print("{:.2f}".format(new_score/mathlogic.pot(tenlog))+"e"+str(tenlog)+" TB")
        mathlogic.Add_toScore(mathlogic.increment())
        mathlogic.AddNumtoItem(1,"Taschenrechner")
        mathlogic.AddPowtoItem(1,"RaspberryPi")
        mathlogic.MultPowofItem(1.01,"Taschenrechner")
        time.sleep(1)
