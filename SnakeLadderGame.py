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
