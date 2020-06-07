#
#
# This is the main file for my game.
# This file will import all the other files to help me break down the game into several smaller files
#
# This is written by Andrew Hitchcock
#
# I started writing this on 5-25-2020
#
#-----------------------------------------------------------------------------------------------------------------------------------------
# This will allow python to look in my current working directory for modules
import os, sys, tools
path = os.getcwd()
sys.path.insert(0,path)

#importing any modules required
import Character_creation, travel

welcome_text = 'Data\\narration\\Welcome_to_Eerda.txt'
tools.read_file(welcome_text, 1.5)

# load character creation script
Character_creation.make_player()
travel.first_travel()