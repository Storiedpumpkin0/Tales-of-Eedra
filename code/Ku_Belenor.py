# The player travels to Ku Belenor
def Ku_belenor():
    import os, sys, tools, time, Derith
    path = os.getcwd()
    sys.path.insert(0,path)

    # Variables
    read_speed = 1.5
    directory = 'Data\\narration\\Navigation\\ku_belenor\\'
    Telmundel_intro = directory + 'elvish_District\\Telmundel_intro.txt'
    if_elf =  directory + 'elvish_District\\if_elf.txt'
    if_dwarf =  directory + 'elvish_District\\if_dwarf.txt'
    Telmundel_continues =  directory + 'elvish_District\\Telmundel_continues.txt'
    seaman_jim =  directory + 'fish_markets\\seaman_jim.txt'
    govoners_file =  directory + 'govoners_palace\\govonor.txt'
    slums_intro =  directory + 'slums\\slums.intro.txt'
    if_rogue =  directory + 'slums\\if_rogue.txt'
    intro_file = 'ku_belenor_intro.txt'
    choices_file = 'Ku_Belenor_choices.txt'
    inn_file =  directory + 'Inn\\Inn_Intro.txt'
    if_hurt =  directory + 'Inn\\if_hurt.txt'
    inn_conclusion =  directory + 'Inn\\Inn_conclusion.txt'
    all_knowing_ones_file =  directory + 'All_Knowing_Ones_booth\\brother_Ku_Belenor.txt'

    # Read the Ku Belenor intro
    tools.read_file(directory + intro_file, read_speed)

    # give the player an option to pick
    while True:
        tools.read_file(directory + choices_file, read_speed)
        print("\n")
        response = input("What will you do?")

        if 'elvish district' in response.lower():
            tools.read_file(Telmundel_intro, read_speed)
            race = tools.get_player_stat('Race')
            time.sleep(read_speed)
            # if the player is an elf, reward them
            if race == 'elf':
                tools.read_file(if_elf, read_speed)
                time.sleep(read_speed)
                tools.player_level_up()
            elif race == 'dwarf':
                tools.read_file(if_dwarf, read_speed)
            else:
                None
            time.sleep(read_speed)
            tools.read_file(Telmundel_continues, read_speed)

        elif 'fish market' in response.lower():
            time.sleep(read_speed)
            tools.read_file(seaman_jim, read_speed)

        elif 'governors palace' in response.lower():
            time.sleep(read_speed)
            tools.read_file(govoners_file, read_speed)

        elif 'slums' in response.lower():
            time.sleep(read_speed)
            tools.read_file(slums_intro, read_speed)
            if tools.get_player_stat('player_class') == 'rogue':
                tools.read_file(if_rogue, read_speed)
            else:
                time.sleep(read_speed)
                print("you find nothing of value")

        elif 'all knowing ones' in response.lower():
            time.sleep(read_speed)
            tools.read_file(all_knowing_ones_file, read_speed)

        elif 'inn' in response.lower():
            time.sleep(read_speed)
            tools.read_file(inn_file, read_speed)

            # If a players health is less than half full the barkeep will offer a health option
            if tools.player_hurt() == True:
                tools.read_file(if_hurt, read_speed)
                time.sleep(read_speed)
                tools.restore_player_hp()
            else:
                None

            tools.read_file(inn_conclusion, read_speed)
        elif 'derith' in response.lower():
            Derith.Derith()
        else:
            print('\n I am sorry, I did not understand you. \n')

        time.sleep(read_speed)
        print("\nyou return to the city\n")
# -------------------------------------------------------------
# DEBUG
Ku_belenor()
