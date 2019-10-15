
"""
Thing tha can make the player during the game:
1- take a cart of the mallet
2-
"""
#class player, who is going to receive all parameters about objects and methods

class Player:

    #object to inizialites all the atributes who contains class player, name, cartnumber, turnplay that player have in the game.
    def __init__(self, name,turnplay, alone):
        self.name= name #name of the player
        self.cartnumber= 5 #number static of carts that you gonna have
        self.turnplay= turnplay #each player have a turn
        self.alone= alone #in case that you prefrer to play alone you are going to play with the machine
        self.carts= {} #here is a dictionary that will contains the values of the carts

"""""
    def inf(self):
        return ( '{} {} {} '.format(self.name, self.cartnumber, self.turnplay))

    def applydecrease(self):
        self.cartnumber= int(self.cartnumber - player.decrease)#int(self.cartnumber)


player1= player("Player 1", 4, 1,)
player2= player("Player 2", 4, 1)
player3= player("Player 3", 4, 1)
player4= player("Player 4", 4, 1)
player1.applydecrease()
player2.applydecrease()
player3.applydecrease()
player4.applydecrease()
print(player1.inf(), player2.inf(), player3.inf(), player4.inf())
print(player.number_of_player)
"""