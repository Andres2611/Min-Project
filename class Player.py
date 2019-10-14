#class player, who is going to receive all parameters about objects and methods
class player:
    decrease= -1
    number_of_player= 0
    #object to inizialites all the atributes who contains class player, name, cartnumber, turnplay that player have in the game.
    def __init__(self, name, cartnumber,turnplay ):
        self.name= name
        self.cartnumber= cartnumber
        self.turnplay= turnplay

        player.number_of_player +=1

    def inf(self):
        return ( '{} {} {} '.format(self.name, self.cartnumber, self.turnplay))

    def applydecrease(self):
        self.cartnumber= int(self.cartnumber - player.decrease)#int(self.cartnumber)


player1= player("Player 1", 4, 1)
player2= player("Player 2", 4, 1)
player3= player("Player 3", 4, 1)
player4= player("Player 4", 4, 1)
player1.applydecrease()
player2.applydecrease()
player3.applydecrease()
player4.applydecrease()
print(player1.inf(), player2.inf(), player3.inf(), player4.inf())
print(player.number_of_player)