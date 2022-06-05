import random
# colorama is inbuilt module for color text in console
from colorama import Fore, Back
# class game is assigned with all the functinality of game.
class Game:
    # welcome message 
    message = """
        Welcome to Snake and Ladder Game.
        Developed by: M.venkateswara Rao
        Select Snake and Ladder data-type:
        --> Enter 1 to select default values for snake and ladder.
        --> Enter 2 to give values manually.
        """
    print("""Fore.LIGHTCYAN_EX """+ message)

    # snake and ladder positions
    # default values to snake 

    # key is head position of snake
    # value is tail position of snake
    # Therefore (key > value) 
    option=int(input('\t'))
    print('\n')
    if option == 1:
        snakes = {
            17:7,
            62:19,
            54:34,
            87:36,
            64:60,
            93:73,
            95:75,
            98:76
    }

    # key is starting position of ladder
    # value is ending position of ladder
    # Therefore (key < value)
        ladders = {
            1:38,
            4:14,
            9:31,
            21:42,
            28:84,
            51:67,
            72:91,
            80:99
        }
        player_one_name = 'Nithya'
        player_one_initial_position = 0
        player_one_final_position = 0

        player_two_name = 'Manjunath'
        player_two_initial_position = 0
        player_two_final_position = 0

    # manual data entry for snakes and ladder
    elif option == 2 :
        message = """
        Rules to follow for snake positions and ladder positions.
        --> There won't be a snake or ladder at 100.
        --> snake and ladder positions shouldn't exceed 100.
        --> There won't be multiple snake or ladder at the tail of the snake, or
            the end position of the ladder and the piece should go up or down accordingly.
        --> Snake and Ladder do not form an infinite loop.
        """
        print(message+'\n')
        no_of_snakes = int(input('Enter total number of snakes in the game '))
        print('Head position of snake should be greater than Tail position of the snake')

    # manual data entry for snake
        snakes = {}
        for i in range(no_of_snakes):
            key=int(input('Enter Head position of snake '+ str(i+1)+'\t'))
            value=int(input('Enter Tail position of snake '+ str(i+1)+'\t'))
            if value < key:
                snakes[key]=value
            else:
                print('Invalid input, Head position of snake should be greater than Tail position of the snake')
                break
        
    # manual data entry for ladder
        no_of_ladders = int(input('Enter total number of ladders in the game '))
        print('Starting position of the ladder should be lesser than the Ending position of the ladder')

        ladders = {}
        for i in range(no_of_ladders):
            key=int(input('Enter starting position of ladder '+ str(i+1)+'\t'))
            value=int(input('Enter ending position of ladder '+ str(i+1)+'\t'))
            if value > key:
                ladders[key]=value
            else:
                print('Invalid input, Ending position of ladder should be greater than Starting position of the ladder')
                break
        
        player_one_name = input('Enter player one name ')
        player_one_initial_position = 0
        player_one_final_position = 0

        player_two_name = input('Enter player two name ')
        player_two_initial_position = 0
        player_two_final_position = 0

   

    def play(self):
        while (self.player_one_final_position <= 100 or self.player_two_final_position <= 100) :
        # player one rolls the dice 
            print(Fore.LIGHTMAGENTA_EX +self.player_one_name +' is playing')
            dice_value = random.choice([1,2,3,4,5,6])
            if self.player_one_final_position + dice_value <= 100 :
                self.player_one_final_position = self.player_one_final_position + dice_value
                print(Fore.LIGHTMAGENTA_EX +self.player_one_name + ' rolled a '+str(dice_value)+' and moved from the position '+str(self.player_one_initial_position)+' to the position '+str(self.player_one_final_position)+'\n')
                self.player_one_initial_position = self.player_one_final_position

            # snake bite checking 
            if self.player_one_initial_position in self.snakes.keys():
                print(Fore.LIGHTRED_EX + 'oh no......!!!!!!!, '+self.player_one_name+' got snake-bite by '+str(self.snakes[self.player_one_initial_position])+' positions')
                self.player_one_final_position = self.snakes[self.player_one_initial_position]
                print(Fore.LIGHTRED_EX + self.player_one_name+' moved down to '+str(self.player_one_final_position)+' position due to snake bite'+'\n')
                self.player_one_initial_position = self.player_one_final_position

            # ladder luck checking
            if self.player_one_initial_position in self.ladders.keys():
                print(Fore.LIGHTGREEN_EX +'woo-hoo..!!, '+self.player_one_name+' got lucky to climb ladder to '+str(self.ladders[self.player_one_initial_position])+' position')
                self.player_one_final_position = self.ladders[self.player_one_initial_position]
                print(Fore.LIGHTGREEN_EX +self.player_one_name+' moved up to '+str(self.player_one_final_position)+' position due to ladder'+'\n')
                self.player_one_initial_position = self.player_one_final_position

            # checking for winner 
            if (self.player_one_final_position == self.player_one_initial_position == 100) :
                print(Fore.LIGHTGREEN_EX + Back.RED +self.player_one_name+' has won the game, Hurray!!!')
                break 
            

        # player two rolls the dice
            print(Fore.LIGHTYELLOW_EX +self.player_two_name +' is playing')
            dice_value = random.choice([1,2,3,4,5,6])
            if self.player_two_final_position + dice_value <= 100 :
                self.player_two_final_position = self.player_two_final_position + dice_value
                print(Fore.LIGHTYELLOW_EX +self.player_two_name + ' rolled a '+str(dice_value)+' and moved from the position '+str(self.player_two_initial_position)+' to the position '+str(self.player_two_final_position)+'\n')
                self.player_two_initial_position = self.player_two_final_position

            # snake bite checking 
            if self.player_two_initial_position in self.snakes.keys():
                print(Fore.LIGHTRED_EX + 'oh no......!!!!!!!, '+self.player_two_name+' got snake-bite by '+str(self.snakes[self.player_two_initial_position])+' positions')
                self.player_two_final_position = self.snakes[self.player_two_initial_position]
                print(Fore.LIGHTRED_EX + self.player_two_name+' moved down to '+str(self.player_two_final_position)+' position due to snake bite'+'\n')
                self.player_two_initial_position = self.player_two_final_position

            # ladder luck checking
            if self.player_two_initial_position in self.ladders.keys():
                print(Fore.LIGHTGREEN_EX +'woo-hoo..!!, '+self.player_two_name+' got lucky to climb ladder to '+str(self.ladders[self.player_two_initial_position])+' position')
                self.player_two_final_position = self.ladders[self.player_two_initial_position]
                print(Fore.LIGHTGREEN_EX +self.player_two_name+' moved up to '+str(self.player_two_final_position)+' position due to ladder'+'\n')
                self.player_two_initial_position = self.player_two_final_position

            # checking for winner
            if (self.player_two_final_position == self.player_two_initial_position == 100) :
                print(Fore.LIGHTGREEN_EX +Back.RED+self.player_two_name+' has won the game, Hurray!!!')
                break 