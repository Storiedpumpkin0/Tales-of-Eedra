# entering the waterm from players first movement choice
def enter_the_water():
    import tools

    read_file = 'Data\\narration\\Navigation\\response1\\response1_enter_the_water.txt'
    death_file = 'Data\\narration\\Navigation\\response1\\octopus_fight_death.txt'
    player_file = 'Data\\player_info\\player.txt'
    escape_file = 'Data\\narration\\Navigation\\response1\\octopus_fight_escape.txt'
    player_info = {}
    read_speed = 1

    # read the prompt for the player
    tools.read_file(read_file, read_speed)

    # open the players info file
    with open(player_file, 'r') as player:
        player_contents = player.read()
        player_info =eval(player_contents)

    # check player's dex
    if player_info['Dex'] > 15 :
        # update the players statistics
        tools.update_player_stats('Dex', player_info['Dex'] + 1)
        tools.read_file(escape_file, read_speed)
        return

    else:
        tools.read_file(death_file, read_speed)
        tools.end()
        return