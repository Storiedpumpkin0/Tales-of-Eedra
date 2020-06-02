# Player choses the path from first travel movement
import tools

welcome_file = 'Data\\narration\\Navigation\\dereth\\welcome_to_derith.txt'
choices_file = 'Data\\narration\\Navigation\\dereth\\derith_choices.txt'
burned_buildings_file = 'Data\\narration\\Navigation\\dereth\\derith_burned_buildings.txt'
court_file = 'Data\\narration\\Navigation\\dereth\\derith_court.txt'
inn_file = 'Data\\narration\\Navigation\\dereth\\derith_inn.txt'
theater_file = 'Data\\narration\\Navigation\\dereth\\derith_theater.txt'
all_knowing_ones_file = 'Data\\narration\\Navigation\\dereth\\derith_all_knowing_ones.txt'

# read the "welcome to derith" file to the player
tools.read_file(welcome_file, 1.5)

while True:

    # read the choices available to the player and record the players choice
    tools.read_file(choices_file,1)
    response = input('What will you do?')

    # If the player chooses to investigate the burned buildings
    if 'burned buildings' in response.lower():
        tools.read_file(burned_buildings_file, 1.5)

    # if a player chooses to go into the court
    elif 'court' in response.lower():
        # open and read the court file
        tools.read_file(court_file, 1.5)

    # If player goes into the inn
    elif 'inn' in response.lower():
       tools.read_file(inn_file, 1.5)

    # if a player goes into the theater
    elif 'theater' in response.lower():
        tools.read_file(theater_file, 1.5)

    # if a player speaks to the all knowing ones booth
    elif 'all knowing ones' in response.lower():
        tools.read_file(all_knowing_ones_file, 1.5)

    elif 'ku belenor' in response.lower():
        print('\n You leave Derith and head north to Ku Belenor')
        import  Ku_Belenor

    elif 'fay' in response.lower():
        print()

    elif 'way' in response.lower():
        print()

    else:
        print('Im sorry, I dont understand what you want.'
              '\n Please choose: BURNED BUILDINGS, COURT, INN, THEATER, ALL KNOWING ONES, KU BELENOR, FEY, WAY')