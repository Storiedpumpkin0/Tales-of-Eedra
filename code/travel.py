# This file will allow players to move through the game.
#
# written by Andrew Hitchcock
#
# Started on 5/25/2020
#
#--------------------------------------------------------------------------------------------------------------------------
import time

# Variables and lists
Narration_folder = 'C:\\Users\\Andrew\\Documents\\D&D\\E\'erda\\Python_Code\\Data\\narration\\Navigation\\'
Awakening = 'Awakening.txt'
response = ''

# Open the awakening file and save the contents
with open (Narration_folder + Awakening, 'r') as file:
   lines = file.readlines()
# Print out the contents with a timed delay, for atmosphere.
for num, line in enumerate(lines, 1):
    print(line)
    #ime.sleep(2)

response = input("What will you do?")

print("you said: ", response)