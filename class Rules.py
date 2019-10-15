class Rules:

    def __init__(self):
        self.quantity_player= 5 #each player has 5 cart on the hands
        self.delete_cart= 1 #every single time that the player have a turn he will delete one cart to have 5  carts
        self.agrupation_cart= 0 #here is the first agrupation of cart that contains 3 or 2 carts of the same value
        self.agrupation_car= 0 #the second agrupation who is going to help us to know if the player win or not will happens same 3 or 2 carts agp
        self.deck_ofcarts= 52 #thats will be the number of carts that will be available to play in the game before give the carts to player
        self.turn_per_player= 1 #each player will have a turn to take a cart to the deck of cart, done all player will star by the firts



