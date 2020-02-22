import time
import random
import sys

# just of effects. add a delay of 1 second before performing any action
PAUSE= 1
MAX_VAL = 100
DICE = 6
# snake takes you down from 'key' to 'value'
snakes = {12: 4, 33: 9, 45: 18, 69: 38, 73: 59, 99: 11}
# ladder takes you up from 'key' to 'value'
ladders = {2: 18, 7: 24, 12: 32, 25: 58, 59: 73, 35: 99}
player_turn_text = [ "Your turn."]
snake_bite = [ "snake bite"]
ladder_jump = ["woohoo"]

def welcome_msg():
    msg = """
    Welcome to Snake and Ladder Game.
    """
    print(msg)

def playernames():
    player1_name = None
    while not player1_name:
        player1_name = input("Enter name of first player: ").strip()
    player2_name = None
    while not player2_name:
        player2_name = input("Enter name of second player: ").strip()
    return player1_name, player2_name
def dice_value():
    time.sleep(PAUSE)
    dice_value = random.randint(1, DICE)
    print("Its a " + str(dice_value))
    return dice_value
def snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper())
    print("\n" + player_name + "  snake bite. Down from " + str(old_value) + " to " + str(current_value))


def ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() )
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))
def check_win(player_name, position):
    time.sleep(PAUSE)
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)

        sys.exit(1)
def snake_ladder(player_name, current_value, dice_value):
    time.sleep(PAUSE)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value
