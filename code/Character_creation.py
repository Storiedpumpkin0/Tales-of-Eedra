# This is a text-based adventure game written by Andrew Hitchcock
#
#
# This file was started on 5/24/2020
#
# This is the "Create your guy/girl" file, being the first file to load when the game is started.
# This file should walk the player through basic character creation.
#
# --------------------------------------------------------------------------------------------------------------------------------------
def make_player():

    #import anything that is needed
    import random,time,tools

    # Variables and lists
    Playable_Races = ('human', 'halfling', 'gnome', 'half orc', 'dwarf', 'half elf', 'elf')
    Playable_Classes = ('sorcerer', 'wizard', 'bard', 'rogue', 'cleric', 'druid', 'monk', 'ranger', 'fighter', 'paladin', 'barbarian')
    Playable_Genders = ('m', 'f')
    player_info_file_path = 'Data\\player_info\\'
    reroll = 'y'
    rollcount = 0
    min = 10
    max = 20

    # Player chooses a race If the race is not found in the list Playable_Races, they must choose again
    race = input("From what race are you? (for help type help)\n").lower()
    while race.lower() not in Playable_Races:
        print( "Please choose one of the following: \n", Playable_Races )
        race = input("From what race are you? \n").lower()
    print("\n Great! so you are a ", race, "\n")

    # Choose Gender and reject invalid input
    gender = input("\nWhat is your gender? (M or F)\n").lower()
    while gender not in Playable_Genders:
        print("I am sorry, please shoose again")
        gender = input("\nWhat is your gender? (M or F)\n")

    # prompt user for name
    player_name = input("\nWhat is your name?")

    # Prompt player to choose class:
    player_class = input("\nWhat is your class? (for help type help)\n").lower()
    while player_class not in Playable_Classes:
        print("Please choose from the following: \n", Playable_Classes)
        player_class = input("\nNow, what is your class?\n")

    # Decide stats
    while reroll == 'y':
        # stats decided at random from min to max
        strength = random.randint(min,max)
        dex = random.randint(min,max)
        con = random.randint(min,max)
        intel = random.randint(min,max)
        wis = random.randint(min,max)
        cha = random.randint(min,max)
        hp = con + strength

        #adjust stats for race
        if race == 'dwarf':
            con = con + 2
            cha = cha - 2
            speed = 20
        elif race == 'elf':
            dex = dex + 2
            con = con - 2
            speed = 30
        elif race == 'gnome':
            con = con + 2
            strength = strength - 2
            speed = 20
        elif race == 'half orc':
            strength = strength + 2
            intel = intel - 2
            cha = cha - 2
            speed = 30
        elif race == 'halfling':
            dex = dex + 2
            strength = strength - 2
            speed = 20
        else:
            speed = 30
            print("\n")

        # put the player info into a dictionary
        player_info_dict = {"Name": player_name,
                            "Race": race,
                            "player_class": player_class,
                            "Gender": gender,
                            "Strength": strength,
                            "Dex": dex,
                            "Constitution": con,
                            "Intelligence": intel,
                            "Wisdom": wis,
                            "Charistma": cha,
                            "Hit Points": hp,
                            "Speed": speed
                            }

        # save the players info as a dictionary in the player info folder
        Newfile = player_info_file_path + "player.txt"
        with open(Newfile, 'w') as file:
           file.write(str(player_info_dict))

        # save the players original information
        Newfile = player_info_file_path + "Original_player.txt"
        with open(Newfile, 'w') as file:
            file.write(str(player_info_dict))

        #Show player stats
        print( "\n\nyour stats are: ")
        time.sleep(1)
        for key in player_info_dict:
            print(key, player_info_dict[key])
            time.sleep(.75)

        # check if the player has rolled too many times
        if rollcount > 1:
            print("\n\nYour fate has been decided")
            break

        # Prompt user to reroll if desiresd, note  a player can only roll 3 times
        adjusted_roll_count = rollcount + 1
        time.sleep(1)
        print("\n\nyou have rolled ", str(adjusted_roll_count), "times already")
        reroll = input("\nIf you dont like your stats, you can re-roll up to two times. would you like to re-roll? (y) ").lower()
        if reroll == 'y' or reroll == 'Y':
            rollcount = rollcount + 1
        else:
            print()

    print("\n great, then your stats are set.")

    return
# -----------------------
# DEBUG
#make_player()