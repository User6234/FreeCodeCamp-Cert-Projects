import copy
import random

class Hat:
    def __init__(self,**kwargs):
        #formats the dictionary into a list of keys using a for loop
        #and multiplies the number of keys by the value for each
        self.b=dict(kwargs)
        self.contents=[]
        for k,v in self.b.items():
            for i in range(v):
                self.contents.append(k)
    
    #string representation, not required but I figured I'd put it in just in case
    #just returns the contents
    def __str__(self):
        return str(f"Hat contains: {self.contents}")
    
    def draw(self,n):
        #draws n balls, if the amount is larger then the length of the list then draws/returns all
        if n>len(self.contents):
            return self.contents
        out=[]
        out=random.sample(self.contents,n)
        #removes the balls from the hat that are drawn
        for i in range(n):
            self.contents.remove(out[i])
        return out

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #final value to be divided by number of experiments
    count=0
    for i in range(num_experiments):
        #ca (current added) is the temporary count that gets reset for each experiment
        ca=0
        #hcop is a copy of the hat
        hcop=copy.deepcopy(hat)
        out=hcop.draw(num_balls_drawn)
        '''
        for each item in the expected_balls dictionary check if it is in the hat
        if it is increment ca, should ca be equal to the amount of entrys in expected_balls
        add 1 to count
        '''
        for k,v in expected_balls.items():
            if out.count(k)>=v:
                ca+=1
            if ca>=len(expected_balls):
                count+=1
    return count/num_experiments

print(Hat(red=3,blue=2))
print(Hat(blue=2,red=3).draw(2))
hat=Hat(blue=3,red=2,green=6)
print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))