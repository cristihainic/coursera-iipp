import random

# helper functions

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Name does not compute."

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Number does not compute."

def rpsls(player_choice): 
    print "Player chooses", player_choice + "."
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice + "."
    difference = (comp_number - player_number) % 5
    CW = "Computer Wins!"
    PW = "Player wins!"
    if difference == 1:
        print CW
    elif difference == 2:
        print CW
    elif difference == 3:
        print PW
    elif difference == 4:
        print PW
    elif comp_number == player_number:
        print "Player and computer tie!"
    else:
        print "You screwed up somewhere; go check your code."
    print "\n" # A blank line looks better at the end of the function than at the beginning.
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
