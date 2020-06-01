# This file will be  a collection of tools that will help in the game

import os
import sys
import tools
import random
path = os.getcwd()
sys.path.insert(0,path)
response1 = ''

def read_file(filename, number):
    import time
    with open(filename, 'r') as file:
        #print('DEBUG',filename)
        lines = file.readlines()
        # Print out the contents with a timed delay, for atmosphere.
    for num, line in enumerate(lines, 1):
        print(line)
        time.sleep(number)
    return

# method to determine if player makes a hit
# provides a max number
def hit_or_miss(limit):
    var = random.randint(0,20)
    player_dex = tools.get_player_stat('Dex')
    if var + player_dex >= limit:
        return 'hit'
    else:
        return 'miss'

# method to update the platers stats
def update_player_stats(key, value):
    player_file = 'Data\\player_info\\player.txt'
    # open the players statistics file
    with open(player_file, 'r') as player:
        player_contents = player.read()
        player_info = eval(player_contents)

    # update the given statistic to the new value
    player_info[key] = value

    # save the new dictionary to the players file
    with open(player_file, 'w') as file:
        file.write(str(player_info))
    return

# get a players stat
def get_player_stat(key):
    player_file = 'Data\\player_info\\player.txt'
    # open the players statistics file
    with open(player_file, 'r') as player:
        player_contents = player.read()
        player_info = eval(player_contents)
        stat = player_info[key]
    return stat

def get_monster_stat(monster_file, stat):
    # open the monster statistics file
    with open(monster_file, 'r') as monster:
        monster_contents = monster.read()
        monster_info = eval(monster_contents)
        stat = monster_info[stat]
    return stat

# method to update a monsters HP after being attacked by the player
def update_monster_hp(monster_file, value):
    # open the monster statistics file
    with open(monster_file, 'r') as monster:
        monster_contents = monster.read()
        monster_info = eval(monster_contents)

    # update the hp to the new value
    monster_info['Hit Points'] = monster_info['Hit Points'] - value

    # save the new dictionary to the monster file
    with open(monster_file, 'w') as file:
        file.write(str(monster_info))
    return

def reset_monster_hp(monster_file, value):
    # open the monster statistics file
    with open(monster_file, 'r') as monster:
        monster_contents = monster.read()
        monster_info = eval(monster_contents)

    # update the hp to the new value
    monster_info['Hit Points'] = value

    # save the new dictionary to the monster file
    with open(monster_file, 'w') as file:
        file.write(str(monster_info))
    return

def end():
    quit = input('press anything to continue ')
    if quit == 'hey dont actually quit':
        print('oh...okay then...')
    else:
        exit()
    return