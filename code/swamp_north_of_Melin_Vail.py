# Player enters the swamp north of Melin Vail

def enter_first_swamp():
    import tools
    import time
    import random

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
    read_time = 1.5
    troll_closer = 0

    #reset the trolls hp
    tools.reset_monster_hp(directory + troll_file, 84)

    tools.read_file(directory + intro_file, read_time)
    tools.read_file(directory + first_choice, read_time)

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
                tools.read_file(directory + run, read_time)
                # Check if players foot comes free
                if tools.hit_or_miss('Dex', 25) == 'hit':
                    tools.read_file(directory + run, read_time)
                    print('\nYour foot comes free!\n')
                    tools.read_file(directory + escape_file, read_time)
                    break
                else:
                    print("\nyou pull, but your foot remains stuck in the mud.")
                    troll_closer = troll_closer + 1
                    if troll_closer > 2:
                        tools.read_file(directory + player_death_file, read_time)
                        tools.end()
                    else:
                        None

            # player chooses to fight the troll
            elif 'weapon' in action.lower():
                if tools.hit_or_miss('Dex', 15) == 'hit':
                    tools.read_file(directory + attack_troll_apears, read_time)
                    time.sleep(read_time)
                    print(' -*- \n troll takes ', str(tools.get_player_stat('Strength')),'damage \n -*-')
                    time.sleep(read_time)
                    # update the trolls hp to reflect damage equal to the players strength
                    tools.update_monster_hp(directory + troll_file, tools.get_player_stat('Strength'))
                    troll_hp = tools.get_monster_stat(directory + troll_file, 'Hit Points')
                else:
                    print("You swing, but you miss")

                # The troll attacks and damage is taken from the players hp equal to the strength og the troll
                time.sleep(read_time)
                print('\nthe troll swings its claws at you')
                time.sleep(read_time)
                time.sleep(read_time)
                    # the trolls base attack is multiplied by a random number from one to 6, then that number is subtracted from the players hp
                damage = tools.get_monster_stat(directory + troll_file, 'Damage') + random.randint(1,6)

                #check to see weather the troll makes a hit or not
                if tools.monster_hit_or_miss(directory+troll_file, 'Dex', 15) == 'hit':
                    tools.update_player_stats('Hit Points', tools.get_player_stat('Hit Points') - damage)
                    time.sleep(read_time)
                    print('\n-*- \nyou take ', damage, 'damage')
                    time.sleep(read_time)
                    print('\nyour new hp is:', tools.get_player_stat('Hit Points'), '\n -*-')
                else:
                    time.sleep(read_time)
                    print("\nthe troll misses\n")
            else:
                print('I am sorry, I do not understand what you want to do')

            if troll_hp <= 0:
                time.sleep(read_time)
                print('the troll falls to the ground, your foot comes free!')
                time.sleep(read_time)
                tools.player_level_up()
                time.sleep(read_time)
                tools.read_file(directory + escape_file, read_time)

            else:
                None

#-------------------------------
# DEBUG
# enter_first_swamp()