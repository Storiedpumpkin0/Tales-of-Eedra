# This file will allow players to move through the game.
#
# written by Andrew Hitchcock
#
# Started on 5/25/2020
#
#--------------------------------------------------------------------------------------------------------------------------

import os, sys, tools, response1_north, response1_south, response1_enter_the_water, Derith
#make the working directory visable to load modules from
path = os.getcwd()
sys.path.insert(0,path)
response1 = ''
read_speed = 1.5

def first_travel():
    import time

    # Variables and lists
    Narration_folder = 'Data\\narration\\Navigation\\'
    Awakening = 'Awakening.txt'

    # Open the awakening file and save the contents
    tools.read_file(Narration_folder + Awakening, read_speed)

    # record user response. ask again
    while True:
        response = input("What will you do?")
        if 'north' in response.lower():
            response1_north.response1_north()
            break
        elif 'south' in response.lower():
            response1_south.response1_south()
            break
        elif 'path' in response.lower():
            print("\n You walk down the path.\n")
            Derith.Derith()
            break
        elif 'water' in response.lower():
            response1_enter_the_water.enter_the_water()
            break
        else:
            print("I am sorry, I don't understand.\n Do you want to go NORTH, SOUTH, down the PATH, or into the WATER?")
    return
#--------------------------------------------------------------------------------------------------------
# DEBUG
#first_travel()