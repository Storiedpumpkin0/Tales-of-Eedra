# Player enters the swamp north of Melin Vail

import tools

directory = 'Data\\narration\\Navigation\\swamps\\swamp_north_of_Melin_Vail\\'
intro_file = 'intro.txt'
first_choice = 'first_choices.txt'
run = 'run.txt'
attack_troll_apears = 'attack_troll_apears.txt'
troll_file = 'troll_stats.txt'
original_troll_file = 'troll_stats_orriginal.txt'
escape_file = 'escape_swamp.txt'
player_death_file = 'troll_kills_player.txt'
troll_hp = tools.get_monster_stat(directory + troll_file, 'Hit Points')
player_hp = tools.get_player_stat('Hit Points')

#reset the trolls hp
tools.reset_monster_hp(directory + troll_file, 15)

tools.read_file(directory + intro_file, 0)
tools.read_file(directory + first_choice, 0)

while troll_hp > 0:
    # check players hp
    player_hp = tools.get_player_stat('Hit Points')
    #print("DEBUG", player_hp)
    if player_hp < 1:
        tools.read_file(directory + player_death_file, 2)
        tools.end()

    else:

        action = input("What do you do?")
         # player chooses to try to pull free of the mud
        if 'foot' in action.lower():
            tools.read_file(directory + run, 0)
            tools.read_file(directory + escape_file, 1)
            break

        # player chooses to fight the troll
        elif 'weapon' in action.lower():
            if tools.hit_or_miss(15) == 'hit':
                tools.read_file(directory + attack_troll_apears, 0)
                print(' --- \n troll takes ', str(tools.get_player_stat('Strength')),'damage')
                # update the trolls hp to reflect damage equal to the players strength
                tools.update_monster_hp(directory + troll_file, tools.get_player_stat('Strength'))
                troll_hp = tools.get_monster_stat(directory + troll_file, 'Hit Points')
            else:
                print("You swing, but you miss")

            # The troll attacks and damage is taken from the players hp equal to the strength og the troll
            print('the troll swings its claws at you')
            tools.update_player_stats('Hit Points', tools.get_player_stat('Hit Points') - tools.get_monster_stat(directory + troll_file, 'Strength'))
            print('your new hp is:', tools.get_player_stat('Hit Points'))

        else:
            print('I am sorry, I do not understand what you want to do')

print('the troll falls to the ground, your foot comes free!')
tools.read_file(directory + escape_file, 1)



