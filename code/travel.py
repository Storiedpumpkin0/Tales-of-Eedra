# This file will allow players to move through the game.
#
# written by Andrew Hitchcock
#
# Started on 5/25/2020
#
#--------------------------------------------------------------------------------------------------------------------------
#make the working directory visable to load modules from

import os
import sys
import tools
path = os.getcwd()
sys.path.insert(0,path)
response1 = ''

def first_travel():
    import time

    # Variables and lists
    Narration_folder = 'Data\\narration\\Navigation\\'
    Awakening = 'Awakening.txt'

    # Open the awakening file and save the contents
    tools.read_file(Narration_folder + Awakening, 1.5)


    # record user response. ask again
    while True:
        response = input("What will you do?")
        if 'north' in response.lower():
            response = 'north'
            break
        elif 'south' in response.lower():
            response = 'south'
            break
        elif 'path' in response.lower():
            response =  'path'
            break
        elif 'water' in response.lower():
            response = 'water'
            break
        else:
            print("I am sorry, I don't understand.\n Do you want to go NORTH, SOUTH, down the PATH, or into the WATER?")
    return response

# Have the player make their first choice of movement
response1 = first_travel()

#respond acording to players response
if response1 == 'water':
    import response1_enter_the_water
elif response1 == 'north':
    import response1_north
elif response1 == 'path':
    import response1_path
else:
    print("Good choice not entering the water!")
