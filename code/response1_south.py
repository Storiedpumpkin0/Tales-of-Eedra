# The player goes south after waking up

south_file = 'Data\\narration\\Navigation\\response1\\response1_south.txt'
south_choices = 'Data\\narration\\Navigation\\response1\\response1_south_choices.txt'

import tools

tools.read_file(south_file, 1.5)

while True:
    tools.read_file(south_choices,1)
    response = input('What do you do?')

    if 'water' in response.lower():
        import response1_enter_the_water
        break
    elif 'swamp' in response.lower():
        print()
    else:
        print('I am sorry, I do not understand.\n ')


