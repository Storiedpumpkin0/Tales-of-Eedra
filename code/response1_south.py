def response1_south():
    # The player goes south after waking up
    import tools, response1_enter_the_water, swamp_north_of_Melin_Vail

    south_file = 'Data\\narration\\Navigation\\response1\\response1_south.txt'
    south_choices = 'Data\\narration\\Navigation\\response1\\response1_south_choices.txt'
    read_speed = 1

    tools.read_file(south_file, read_speed)

    while True:
        tools.read_file(south_choices,read_speed)
        response = input('What do you do?')

        if 'water' in response.lower():
            response1_enter_the_water.enter_the_water()

        elif 'swamp' in response.lower():
            swamp_north_of_Melin_Vail.enter_first_swamp()
            # print an error message if the player makes it back here.
            print("\n ------------------------------------------\n"
                  "\nERROR -- ERROR -- ERROR -- THE PROGRAM HAS BROKEN.\n "
                  "THIS MESSAGE IS INSIDE RESPONSE1_SOUTH.py"
                  "\n -------------------------------------------\n")
            tools.end()
        else:
            print('I am sorry, I do not understand.\n ')
    return

#-------------------------------------------------------------------------------
# DEBUG
#response1_south()