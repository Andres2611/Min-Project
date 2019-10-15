#class that is going to contain values and define all atributes that have a cart

class Carts:

    #Meth contructor who define all atributes to use in this class
    def __init__(self, number, color, simbol):
        self.number= number
        self.color= color
        self.simbol= simbol
        self.name= str(number) + simbol
        self.limit= 52

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
            simbol= ' Heart'
            color= ' Red '

        elif(i <= 26):
            simbol= ' Clover'
            color = ' Black '

        elif(i <= 39):

            simbol= ' Espade'
            color= ' Black '

        else:
            simbol= ' Diamond'
            color= ' Red '

        print (str(name) + color + simbol )
        if number==13:
            number =1
        else:
            number +=1
        i+=1


#carta1= carts(10,"Black","Espade")
#carta1.createcart()

createcart()