#class that is going to contain values and define all atributes that have a cart

class Carts:

    #Meth contructor who define all atributes to use in this class
    def __init__(self, number, color, simbol):
        self.number= number #quantity of each cart
        self.color= color #the color will be red or black
        self.simbol= simbol #the simbol can be Spades, Heart, Clover or Diamond
        self.name= str(number) + simbol #name is a concatenation of number and simbol
        self.limit= 52 #the limit of the carts is 52 only

    def look(self):
        pass

    def notlook(self):
        pass


def createcart():
    i=1
    number =1
    limit= 52


    while i <= limit:
        name = number
        if(i<=13):
            simbol= ' ♥ '
            color= ' Red '

        elif(i <= 26):
            simbol= ' ♣ '
            color = ' Black '

        elif(i <= 39):

            simbol= ' ♠ '
            color= ' Black '

        else:
            simbol= ' ♦ '
            color= ' Red '

        print (simbol + str(name) + color + simbol )
        if number==13:
            number =1
        else:
            number +=1
        i+=1


#carta1= carts(10,"Black","Espade")
#carta1.createcart()

createcart()