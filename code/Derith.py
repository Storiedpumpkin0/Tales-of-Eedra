def Derith():
    # Player choses the path from first travel movement
    import tools, Ku_Belenor

    Derith_file_path = 'Data\\narration\\Navigation\\dereth\\'
    welcome_file = Derith_file_path +  'welcome_to_derith.txt'
    choices_file = Derith_file_path + 'derith_choices.txt'
    burned_buildings_file = Derith_file_path + 'derith_burned_buildings.txt'
    court_file = Derith_file_path + 'derith_court.txt'
    inn_file = Derith_file_path + 'derith_inn.txt'
    theater_file = Derith_file_path + 'derith_theater.txt'
    all_knowing_ones_file = Derith_file_path + 'derith_all_knowing_ones.txt'
    read_speed = 1

    # read the "welcome to derith" file to the player
    tools.read_file(welcome_file, read_speed)

    while True:

        # read the choices available to the player and record the players choice
        tools.read_file(choices_file,read_speed)
        response = input('What will you do?')

        # If the player chooses to investigate the burned buildings
        if 'burned buildings' in response.lower():
            tools.read_file(burned_buildings_file, read_speed)
        # if a player chooses to go into the court
        elif 'court' in response.lower():
            # open and read the court file
            tools.read_file(court_file, read_speed)
        # If player goes into the inn
        elif 'inn' in response.lower():
            tools.read_file(inn_file, read_speed)
            tools.restore_player_hp()
        # if a player goes into the theater
        elif 'theater' in response.lower():
            tools.read_file(theater_file, read_speed)
        # if a player speaks to the all knowing ones booth
        elif 'all knowing ones' in response.lower():
            tools.read_file(all_knowing_ones_file, read_speed)
        # if a player choses to go to Ku Belenor
        elif 'ku belenor' in response.lower():
            print('\n You leave Derith and head north to Ku Belenor')
            Ku_Belenor.Ku_belenor()
        # if a player choses to go to Fay
        elif 'fay' in response.lower():
            print()
        # if a player choses to go to Wey
        elif 'way' in response.lower():
            print()
        # if a player does not enter a valid response
        else:
            print('Im sorry, I dont understand what you want.'
               '\n Please choose: BURNED BUILDINGS, COURT, INN, THEATER, ALL KNOWING ONES, KU BELENOR, FEY, WAY')
    return