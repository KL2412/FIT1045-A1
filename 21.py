"""
Group name:If Error Then No Sleep
Authors:Khai Loong Lim
        Andy Tjandra
        Nicholas Tian Quan Wong
        Taha Asghar Chaudhary
"""

import time
import random

def display_rules():
    '''
    Purpose: To print the rules of the game.

    Argument: No argument

    No return value

    Function body: Printing the rules with one print statement then return to caller function
    '''

    #printing the rules of the game so that the user is familiar with the layout and how the game works
    print("""
  _____________________________________________________________________________
  Twenty One is a game of chance where players take turns rolling two dice every 
  round until they decide to stop rolling and lock in their score or end up 
  going bust with a total over 21. The objective is to be the closest to 21 
  when everyone is done rolling.

  Rules are as per follows:
    - Players begin with a score of 0.
    - Each player has one turn to either roll or stop rolling each round.
    - Players can only do a regular roll of two dice until they 
      reach a score of at least 14.
    - Players with a score >= 14 have the option to only roll one dice.
    - If a player scores more than 21 they go bust and are out of the game.
    - The winning player is the one with the score closest to 21 when everyone 
      has finished rolling.
    - If all players go bust, no one wins.
    - If more than one player has the winning score, no one wins.
  _____________________________________________________________________________
  """)
    input("Press enter to go back")
    return


def display_main_menu():
    '''
    Purpose: To print the main menu of the game and let player decide what to do.

    Argument: No argument

    No return value

    Function body: Printing the menu then return to caller function
    '''

    print("------------Main Menu------------")
    print("Welcome to Twenty One!")
    print("1. Solo")
    print("2. Local Multiplayer")
    print("3. Rules")
    print("4. Exit")
    print("---------------------------------")

def int_input(prompt="", restricted_to=None):
    """
    Helper function that modifies the regular input method,
    and keeps asking for input until a valid one is entered. Input
    can also be restricted to a set of integers.

    Arguments:
      - prompt: String representing the message to display for input
      - restricted: List of integers for when the input must be restricted
                    to a certain set of numbers

    Returns the input in integer type.
    """
    #this while loop checks whether the user enters a valid input according the options prompted
    while True:
        player_input = input(prompt)
        try:
            int_player_input = int(player_input)
        except ValueError:
            continue
        if restricted_to is None:
            break
        elif int_player_input in restricted_to:
            break

    return int_player_input
    

def cpu_player_choice(score):
    """
    Purpose: This function simply returns a choice for the CPU player based on their score.

    Arguments:
      - score: Int

    Returns an int representing a choice from 1, 2 or 3.
    """
    time.sleep(2)
    #this if/else loop initializes the choices as user has based on their score i.e. whether
    #they have gone bust, are valid or can still roll
    if score < 14:
        return 1
    elif score < 17:
        return 3
    else:
        return 2



def display_game_options(player):
    """
    Purpose: Prints the game options depending on if a player's score is >= 14.

    Arguments:
      - player: A player dictionary object

    No return value

    Function body:
        -Prints player's current score
        -If player's score < 14, display two options (1. Roll and 2. Stay)
        -If player's score >= 14, display an extra option (3.Roll One)
    """

    #prints the header of game option
    print("------------" + player["name"] + "'s turn------------")
    #prints player's current score
    print(player['name'] + "'s score: " + str(player['score']))
    #print game options according to the player's score
    print("1. Roll" + "\n2. Stay")
    if player['at_14']:
        print("3. Roll One")

def display_round_stats(round, players):
    """
    Purpose: Print the round statistics provided a list of players.

    Arguments:
      - round: Integer for round number
      - players: A list of player-dictionary objects

    Return value: No return Value

    Function body:
        print the round statistics header
        for loop to iterate through every element in players
            print the name and score of the player
    """
    #print round header with string concatenation
    print("-----------Round " + str(round) + "-----------")
    #iterate through every player in players with a for loop and print every players' name and score
    for player in players:
        print(player['name'] + " is at " + str(player['score']))

def roll_dice(num_of_dice=1):
    """
    Purpose: Rolls dice based on num_of_dice passed as an argument.
    
    Arguments:
      - num_of_dice: Integer for amount of dice to roll

    Returns the following tuple: (rolls, display_string)
      - rolls: A list of each roll result as an int
      - display_string: A string combining the dice art for all rolls into one string

    Function Body:
        declare an empty list called rolls
        for loop (loops n times where n = number of dice)
            append a random value between 1 to 6 into rolls

        declare an empty string variable called display_string
        declare i = 0 (to use as index for die_art)
        while loop to iterate 5 times
            for loop to iterate through every element in rolls
                append the die art for every number in rolls
            append a newline to the string

    Visualisation example:
        let rolls = [1, 2]
        In the nested loop, 
            "┌─────────┐" and "┌─────────┐" will be appended to the string first followed by a \n
            "│         │" and "│  ●      │" will be appended next then
            "│    ●    │" and "│         │" then
            "│         │" and "│      ●  │" then
            "└─────────┘" and "└─────────┘" will be appended last
    """

    #provided die art
    die_art = {
        1: ["┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"],
        2: ["┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"],
        3: ["┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"],
        4: ["┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"],
        5: ["┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"],
        6: ["┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"]
    }

    #create a list of dice rolls by generating random integers between 1 to 6 (inclusive)
    rolls = []
    for i in range(num_of_dice):
        rolls.append(random.randint(1, 6))

    #create a string that contains die art containing every element in the list of rolls
    display_string = ''
    i = 0
    while i < 5:
        for j in rolls:
            display_string += die_art[j][i]
        i += 1
        display_string += '\n'

    #return rolls and display_stirng in tuple form (immutable)
    return (rolls, display_string)

def execute_turn(player, player_input):
    '''
    Purpose:Execute every turn after player chooses which move to take.
            Print the die of the rolled values
            Update the values of the player in their respective dictionary
            Display the effect of their move (stayed/busted)
            Display the score of the player after current round
    
    Argument:
       - player: A player dictionary object
       - player_input: Player's move chosen (1 - Roll both, 2 - Stay, 3 - Roll One)

    Return Value:
    - player: A player dictionary object (updated values)

    Funtion Body:
        If player chooses to roll both:
            Display "Roll Both..."
            call roll_dice() function
            display the die rolled
            add values of the die into player score
        If player chooses to stay:
            Display string to indicate that the player had stayed with x score
            change the value of 'stayed' in dictionary to True
        If player chooses to roll one:
            Display "Rolling One..."
            call roll_dice() function
            display the die rolled
            add value of the die into player score
        
        check the score of the player
            if >= 14, update 'at_14' to True
            if > 21, display name and score of player then update 'bust' to True 

        
        Display name and score of player if the player is not bust and not stayed
    '''
    #carry out different task according to player's game option
    if player_input == 1:
        # roll both
        print("Rolling both...")
        rolls, display_string = roll_dice(2)
        print(display_string)
        for i in rolls:
            player['score'] += i
    elif player_input == 2:
        # stay
        print(player['name'] + " has stayed with a score of " + str(player['score']))
        player['stayed'] = True
        return player
    elif player_input == 3:
        # roll one
        print("Rolling one...")
        rolls, display_string = roll_dice()
        print(display_string)
        player['score'] += rolls[0]

    #check player's score and update respective fields (score/at_14/bust) if needed
    if player['score'] >= 14:
        player['at_14'] = True
        if player['score'] > 21:
            print(player['name'] + " is now on " + str(player['score']))
            print(player['name'] + " goes bust!")
            player['bust'] = True
            return player

    #display name and score if the player had not stayed
    print(player['name'] + " is now on " + str(player['score']))

    return player

def end_of_game(players):
    """
    Function:Takes the list of all players and determines if the game has finished,
             returning false if not else printing the result before returning true.

    Arguments:
      - players: A list of player-dictionary objects

    Returns True if round has ended or False if not. If true results are
    printed before return.

    Function Body:
        while loop to iterate through players
            if any of the players had not stayed or busted then game is not OverflowError
        
        if game is over
            determine what to display
            return True
    """
    iterator_1 = 0      #initailize as 0 for iteration
    game_over = True    #initialize game over as True as default
    number_of_bust = 0  #initialize as 0 to check number of bust
    high_score = -1     #initialize as -1 instead of 0 because player's default score at first is 0
    winner_player = ""  #initialize as "" to store the winner's name

    #check if the game has over or no, if no, return false
    while (iterator_1 < len(players)):
        #check the condition of each player for bust and stay status
        if (not (players[iterator_1]['stayed'])) and (not (players[iterator_1]['bust'])):
            game_over = False
            return False

        iterator_1 = iterator_1 + 1

    #if game has rounded or game_over == True
    if game_over:
        #iterate through players
        for iterator_2 in range(len(players)):
            #count the number of bust
            if (players[iterator_2]['bust'] == True):
                number_of_bust = number_of_bust + 1

            #if there is a high score, store the value into high_score and the player's name into winner_player
            if (players[iterator_2]['score'] <= 21 and players[iterator_2]['score'] > high_score):
                high_score = players[iterator_2]['score']
                winner_player = players[iterator_2]['name']

            #display game is draw if there are 2 same high score values
            elif (players[iterator_2]['stayed'] and players[iterator_2]['score'] == high_score):
                print("The game is a draw! No one wins :(")
                return True
    
        #display no one wins if everyone is busted
        if number_of_bust == len(players):
            print("Everyone's gone bust! No one wins :(")
            return True
        
        #display the winner 
        print(winner_player + " is the winner!")
    return True

def solo_game():
    """
    Function: This function defines a game loop for a solo game of Twenty One against AI.

    Arguments: No Arguments

    No return value

    Function body: 
        Initialize 2 players (CPU Player and Player 1)

        While game has not ended
            for every player in players (to iterate through every player in players)
                if player is not bust and had not stayed, then player can carry out game option
    """
    players = [{'name': 'Player 1', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False},
               {'name': 'CPU Player', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}]
    #iterate a scenario in which player 1 plays with the CPU
    game_round = 0
    #while loop that loops until the game had ended
    while not end_of_game(players):
        display_round_stats(game_round, players)
        #for loop to iterate through players
        for player in players:
            #player will only be able to choose game option if the player has not bust and has not stayed
            if not player['bust'] and not player['stayed']: 
                display_game_options(player)
                if player['name'] != 'CPU Player':
                    # normal player
                    if player['score'] >= 14:
                        choice = int_input(prompt="Please enter an option: ",
                                           restricted_to=[1, 2, 3])  # if score is larger than 14
                    else:
                        choice = int_input(prompt="Please enter an option: ",
                                           restricted_to=[1, 2])  # if score is smaller than 14
                else:
                    # cpu player
                    choice = cpu_player_choice(player['score'])
                player = execute_turn(player, choice)
        #next round
        game_round += 1

def multiplayer_game(num_of_players):
    """
    Function: This function defines a game loop for a local multiplayer game of Twenty One, 
              where each iteration of the while loop is a round within the game. 

    Argument: number of players for multiplayer game

    No return value

    Function body:
        Create n players into the variable named players (n = num_of_players from argument)
        Loop while the game have not end(checked by calling end_of_game function) [each loop means one round]
            Display round status
            For loop to iterate through every player in players
                If the player is not busted and has not stayed, he can carry out an action
                Call execute_turn() function
            game_round += 1 (proceed to next round)

    """
    #create n number of player dictionary into players using a for loop where n = num_of_players from argument
    players = []
    for i in range(num_of_players):
        players.append({'name': 'Player ', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False})
        players[i]['name'] += str(i + 1)

    #game loop that keeps looping if the game has not ended
    game_round = 0
    while not end_of_game(players):
        display_round_stats(game_round, players)
        #iterate through every player, if the player is not busted or stayed then the player is eligible to choose a game option to continue playing
        for player in players:
            if not player['bust'] and not player['stayed']:
                display_game_options(player)
                if player['score'] >= 14:
                    choice = int_input(prompt="Choice: ", restricted_to=[1, 2, 3])
                else:
                    choice = int_input(prompt="Choice: ", restricted_to=[1, 2])
                player = execute_turn(player, choice) 
        #proceed to next round
        game_round += 1

def main():
    """
    Purpose:Defines the main loop that allows the player to start a game, view rules or quit.

    Argument: No argument

    No return value

    Function body:
        Infinity loop until user chooses to exit the game
        In loop:
            Display the menu
            Prompt user for game options
            call the respective function
    """
    #infinity loop until user enter 4(exit)
    while True:
        display_main_menu()
        choice = int_input(prompt="Please enter an option: ", restricted_to=[1, 2, 3, 4])
        #call the functions that are respective to the chosen option
        if choice == 1:
            solo_game()
        elif choice == 2:
            # prompt num_of_players
            num_of_players = int_input(prompt="Number of players: ", restricted_to=list(range(2, 101)))
            multiplayer_game(num_of_players)
        elif choice == 3:
            display_rules()
        else:
            break

#calling the main function will make the whole game run as every other function will be called from main function.
main()



