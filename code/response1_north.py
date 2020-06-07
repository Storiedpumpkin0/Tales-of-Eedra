
def response1_north():
    # Player choses north from first travel movement
    import tools, Ku_Belenor, response1_enter_the_water

    north_file = 'Data\\narration\\Navigation\\response1\\response1_north.txt'
    read_speed = 1

    # read the response1_north text file
    tools.read_file(north_file, read_speed)

    while True:
        # Read players choice
        response = input('what would you like to do?')
        if 'city' in response.lower():
            Ku_Belenor.Ku_belenor()
        elif 'water' in response.lower():
            print('you enter the water')
            response1_enter_the_water.enter_the_water()
            break
        else:
            print("\nI am sorry, I don't understand. Please chose NORTH, CITY, or WATER\n")
        return
# ___________________________________________________________-
# Debug
#response1_north()