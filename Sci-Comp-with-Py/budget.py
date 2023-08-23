from math import floor

class Category:
    #Get the initial variables set up
    def __init__(self, name):
        self.totplus=0
        self.totminus=0
        self.name=name
        self.ledger=[]
        self.bal=0
        self.l1=""

    #set up the printing format
    def __str__(self):
        n=30-len(self.name)
        for i in range(floor(n/2)):
            self.l1+="*"
        self.l1+=self.name
        for i in range(floor(n/2)):
            self.l1+="*"
        led=""
        for i in self.ledger:
            #Getting the width, var1, and var2 variables set up
            wd=""
            v2=str(i['amount'])[:7]
            v1=i['description'][:23]
            if "." not in str(i['amount']):
              #doing math to get total length for spaces (with .00 on the end for if it's not there normally)
                n2=30-len(f"{i['description'][:23]}{str(i['amount'])+'.00'[:7]}")
                for i in range(n2):
                    wd+=" "
                #commiting to ledger
                led+=f"{v1}{wd}{str(v2)+'.00'[:7]}\n"
            else:
                #doing math to get total length for spaces
                n2=30-len(f"{i['description'][:23]}{str(i['amount'])[:7]}")
                for i in range(n2):
                    wd+=" "
                #commiting to ledger
                led+=f"{v1}{wd}{v2}\n"
        #returning formatted ledger
        return (f"{self.l1}\n{led}Total: {self.get_balance()}")
    
    def deposit(self, amt, dsc=""):
        #setting up variable and adding to the ledger, current balance, and total plus value
        val={"amount": amt, "description": dsc}
        self.ledger.append(val)
        self.bal+=amt
        self.totplus+=amt
    
    def withdraw(self, amt, dsc=""):
        #setting up variable and adding to ledger/taking away from balance if the current balance is higher than the withdraw amount
        val={"amount": -amt, "description": dsc}
        if amt>self.get_balance():
            return False
        else:
            self.ledger.append(val)
            self.bal-=amt
            #and adding a negative value to total minus too
            self.totminus-=amt
            return True
    
    def get_balance(self):
        #returning current balance
        return self.bal
    
    def transfer(self, amt, cat):
        #moving value from one budget to another if the donor has the funds to spare
        if amt>self.get_balance():
            return False
        else:
            self.withdraw(amt, f"Transfer to {cat.name}")
            cat.deposit(amt, f"Transfer from {self.name}")
            return True
    
    def check_funds(self, amt):
        #checking if the user has the requested value in the selected budget
        if amt>self.get_balance():
            return False
        else:
            return True
    
    def spent_percent(self):
        #calculates the amount spent
        return (((self.totplus-self.totminus)/self.totplus)-1)*100

#Format the text vertically
def vertical(categories):
    out=""
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[0]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[1]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[2]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[3]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[4]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[5]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[6]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[7]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[8]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[9]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[10]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[11]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[12]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[13]+"  "
        except:
            out+="   "
    out+="\n"
    out+="     "
    for cat in categories:
        try:
            out+=cat.name[14]+"  "
        except:
            out+="   "
    return out


#Make a chart
#(It was unclear how the numbers should be formatted with the provided description so I made it calculate the % spent from the initial 
#total. This is incorrect as it fails the test, however it would be a reasonably easy fix with more detail)
def create_spend_chart(categories):
    chart="Percentage spent by category\n"
    for i in range(100, -1, -10):
        if i<100:
            if i==0:
                chart+="  "+str(i)+"|"
            else:
                chart+=" "+str(i)+"|"
        else:
            chart+=f"{i}|"
        for cat in categories:
            if cat.spent_percent()>=i:
                chart+=" o "
            else:
                chart+="   "
        chart+="\n"
    chart+="    ----------\n"
    chart+=vertical(categories)

    return chart