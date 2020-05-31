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
import os
import sys
path = os.getcwd()
sys.path.insert(0,path)

#importing any modules required
import Character_creation

# load character creation script
Character_creation.make_player()
import travel
