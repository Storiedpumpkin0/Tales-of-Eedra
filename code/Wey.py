# Player chooses to go to Wey

def Wey():
    import os, sys, tools, time, Derith
    path = os.getcwd()
    sys.path.insert(0,path)

    #variables
    Wey_file_path = 'Data\\narration\\Navigation\\Wey\\'
    Wey_intro = 'wey.txt'
    inn_file = 'Wey_inn.txt'
    adventure_market = 'adventure_market.txt'
    adventure_market_again = 'adventure_market_again.txt'
    choices_file = 'wey_choices.txt'
    read_speed = .1
    number_adventure_market = 0


    tools.read_file(Wey_file_path + Wey_intro, read_speed)

    while True:
        tools.read_file(Wey_file_path + choices_file, read_speed)
        response = input("What do you do?")

        if 'inn' in response.lower():
            time.sleep(read_speed)
            tools.read_file(Wey_file_path + inn_file, read_speed)

        elif 'adventure market' in response.lower():
            number_adventure_market = number_adventure_market + 1
            time.sleep(read_speed)
            if number_adventure_market <= 1:
                tools.read_file(Wey_file_path + adventure_market, read_speed)
                tools.player_level_up()
            else:
                tools.read_file(Wey_file_path + adventure_market_again, read_speed)
        elif 'hobble hill' in response.lower():
            print()
        elif 'Derith' in response.lower():
            time.sleep(read_speed)
            print("you ", response)
            Derith.Derith()
        elif "east" in response.lower():
            print()
        else:
            print(" \n\n\t\t I am sorry, I dont understand\n")

    return
#-------------------------------------------------------------------
# DEBUG
Wey()