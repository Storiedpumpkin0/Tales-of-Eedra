# Player choses north from first travel movement
import tools

north_file = 'Data\\narration\\Navigation\\response1\\response1_north.txt'

# read the response1_north text file
tools.read_file(north_file, 2)

while True:
    # Read players choice
    response = input('what would you like to do?')
    if 'north' in response.lower():
        print('You go north again')
        break
    elif 'city' in response.lower():
        import Ku_Belenor
    elif 'water' in response.lower():
        print('you enter the water')
        import  response1_enter_the_water
        break
    else:
        print("\nI am sorry, I don't understand. Please chose NORTH, CITY, or WATER\n")


