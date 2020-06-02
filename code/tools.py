# This file will be  a collection of tools that will help in the game

import os
import sys
import tools
import random
import pprint
import time
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
def hit_or_miss(stat, limit):
    var = random.randint(0,20)
    player_stat = tools.get_player_stat(stat)
    if var + player_stat >= limit:
        return 'hit'
    else:
        return 'miss'

def restore_player_hp():
    # open the monster statistics file
    player_file = 'Data\\player_info\player.txt'
    original_player_file = 'Data\\player_info\\Original_player.txt'
    with open(player_file, 'r') as player:
        player_contents = player.read()
        player_info = eval(player_contents)
    #get original health
    with open(original_player_file, 'r') as original_player:
        original_player_contents = original_player.read()
        original_player_info = eval(original_player_contents)
        original_hp = original_player_info['Hit Points']
    # update the hp to the original new value
    player_info['Hit Points'] = original_hp
    # save the new dictionary to the monster file
    with open(player_file, 'w') as file:
        file.write(str(player_info))
    return

# method to update the players stats
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

def player_level_up():
    print("\n -*- \nPLAYER LEVEL UP!\n")
    time.sleep(2)
    player_file = 'Data\\player_info\\player.txt'
    original_player_file = 'Data\\player_info\\Original_player.txt'
    # restore hp before leveling up
    tools.restore_player_hp()
    # open the players statistics file
    with open(player_file, 'r') as player:
        player_contents = player.read()
        player_info = eval(player_contents)
    # get a new dictionary to save the stats to
    player_info = {         "Name": tools.get_player_stat('Name'),
                            "Race": tools.get_player_stat('Race'),
                            "player_class": tools.get_player_stat('player_class'),
                            "Gender": tools.get_player_stat('Gender'),
                            "Strength": tools.get_player_stat('Strength') + 3,
                            "Dex": tools.get_player_stat('Dex') + 3,
                            "Constitution": tools.get_player_stat('Constitution') + 3,
                            "Intelligence": tools.get_player_stat('Intelligence') + 3,
                            "Wisdom": tools.get_player_stat('Wisdom') + 3,
                            "Charistma": tools.get_player_stat('Charistma') + 3,
                            "Hit Points": tools.get_player_stat('Hit Points') + 3,
                            "Speed" : tools.get_player_stat("Speed")
                    }
    # show the player their new stats
    print(" \nYour new stats are as follows:\n")
    pprint.pprint(player_info)

    print('\n -*- \n \n ')
    # save the new dictionary to the players file
    with open(player_file, 'w') as file:
        file.write(str(player_info))

    # save the new dictionary to replace the original stats file
    with open(original_player_file, 'w') as file:
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

def monster_hit_or_miss(monster_file, stat, limit):
    var = random.randint(0,20)
    monster_stat = tools.get_monster_stat(monster_file, stat)
    #if the random number plus the value of the stat is larger then the limmit value, the monster lands a hit
    if var + monster_stat >= limit:
        return 'hit'
    else:
        return 'miss'

def end():
    quit = input('press anything to continue ')
    if quit == 'hey dont actually quit':
        print('oh...okay then...')
    else:
        exit()
    return


#--------------
# Debugs
tools.player_level_up()