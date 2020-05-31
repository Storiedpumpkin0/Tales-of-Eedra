# This file will be  a collection of tools that will help in the game

def read_file(filename, number):
    import time
    with open(filename, 'r') as file:
        #print('DEBUG',filename)
        lines = file.readlines()
        # Print out the contents with a timed delay, for atmosphere.
    for num, line in enumerate(lines, 1):
        print(line)
        time.sleep(number)
    return


