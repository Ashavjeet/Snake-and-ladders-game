import random

def get_players_list():
    name_list= []
    player_1= input("Please enter the name of player 1: ")
    player_2= input("Please enter the name of player 2: ")
    name_list.append(player_1)
    name_list.append(player_2)
    print ("List of players: ",name_list)
    return name_list

def generate_ladders_position():
    ladders_list= []
    while len(ladders_list)!=15:
        i=random.randint(5,85)
        if i not in ladders_list:
            ladders_list.append(i)
    print ("Ladder cells: ",ladders_list)
    return ladders_list

def generate_snake_position(ladders_list):
    snakes_list= []
    while len(snakes_list)!=10:
        i=random.randint(20,95)
        if i not in ladders_list:
            if i not in snakes_list:
                snakes_list.append(i)
    print ("Snake cells: ",snakes_list)
    return snakes_list

def roll_dice(current_position,player_name):
    i=random.randint(1,6)
    new_position= i + current_position
    print (player_name,"dice is: ",i,",","New position is: ",new_position)
    return new_position

def check_for_ladder(current_position,ladders_list,player_name):
    if current_position in ladders_list:
        new_position= current_position + 15
        print("Great,",player_name,"! It's a ladder, Climb up by 15 cells.Your new position is",current_position)
    else:
        new_position= current_position
    return new_position

def check_for_snake(current_position,snakes_list,player_name):
    if current_position in snakes_list:
        new_position= current_position - 10
        print("Oops,",player_name,"! You've been bitten, go down 15 cells.Your new position is",current_position)
    else:
        new_position= current_position
    return new_position

players_position=[0,0]
players_name= get_players_list()
ladders_list= generate_ladders_position()
snakes_list= generate_snake_position(ladders_list)
while players_position[0]<99 or players_position[1]<99:
    for i in range (2):
        players_position[i]= roll_dice(players_position[i],players_name[i])
        if players_position[i] > 99:
            print("\nHuraaaay!  Winner is,",players_name[i],"\n")
            input("Press any key to exit.")
            exit()
        else:
            players_position[i]= check_for_ladder(players_position[i],ladders_list,players_name[i])
            players_position[i]= check_for_snake(players_position[i],snakes_list,players_name[i])
    print()