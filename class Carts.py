#class that is going to contain values and define all atributes that have a cart
import array
from random import shuffle
import random
class carts:
    position = [0,1]
    decrease = -1
    #Meth contructor who define all atributes to use in this class
    def __init__(self,number=52, color=["Black", "Red"], simbol=["Heart", "Diamond", "Clover"], quantity=[1,2,3,4,5,6,7,8,9,10,11,12,13]):
        self.number= number
        self.color= color
        self.simbol= simbol
        self.quantity= quantity
    #Function Whos Choose the Color of the cart
    def choicecolor(self):
        return (random.choice(carts.position))
    #Here we Print All
    def print(self):
        print ('{} {} {} {}'.format (self.number, self.color[1],self.simbol[1], self.quantity[4]))



cart1= carts()
print(cart1.print())