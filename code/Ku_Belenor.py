# The player travels to Ku Belenor

#import stuff
import os
import sys
import tools
path = os.getcwd()
sys.path.insert(0,path)

# Variables
read_speed = 1
directory = 'Data\\narration\\Navigation\\ku_belenor\\'
intro_file = 'ku_belenor_intro.txt'

tools.read_file(directory + intro_file, read_speed)
