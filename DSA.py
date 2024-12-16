import random

# Define the ladders and snakes as dictionaries
# Keys are positions of ladders/snakes, and values are the positions they lead to
ladders = {
    2: 23,
    8: 34,
    20: 77,
    32: 68,
    41: 79,
    74: 92
}

snakes = {
    29: 7,
    38: 15,
    50: 5,
    63: 22,
    86: 36,
    97: 42
}

counter = 0  # To count the number of dice rolls

def dice():
    global counter
    counter += 1
    return random.randint(1, 6)

def move_player(position):
    roll = dice()
    print(f"Rolled a {roll}")
    position += roll

    if position in ladders:
        print(f"Ladder! Climb up from {position} to {ladders[position]}")
        position = ladders[position]
    elif position in snakes:
        print(f"Snake! Slide down from {position} to {snakes[position]}")
        position = snakes[position]

    return position

def game_play(player1, player2):
    position1 = 0
    position2 = 0
    print(f"{player1} and {player2} start the game!")
    while position1 < 100 and position2 < 100:
        # Player 1's turn
        print(f"{player1} is at position {position1}")
        print(f"{player2} is at position {position2}")
        position1 = move_player(position1)
        position2 = move_player(position2)
        while (position1 or position2) > 100:
            print(f"{player1} overshot the finish line. Rolling again!")
            print(f"{player2} overshot the finish line. Rolling again!")
            position1 = move_player(position1 - dice())
            position2 = move_player(position2 - dice())
        if (position1 or position2) == 100:
            print(f"{player1} has won the game!")
            print(f"{player2} has won the game!")
            return player1 or player2

        # Player 2's turn
        # print(f"{player2} is at position {position2}")
        # position2 = move_player(position2)
        # while position2 > 100:
        #     print(f"{player2} overshot the finish line. Rolling again!")
        #     position2 = move_player(position2 - dice())
        # if position2 == 100:
        #     print(f"{player2} has won the game!")
        #     return player2

print("------------ Welcome to Snake and Ladder Game --------------")
player1 = input("Player 1: Enter your name: ")
player2 = input("Player 2: Enter your name: ")

# Randomly decide who starts
if random.randint(0, 1) == 0:
    print(f"{player1} will start first.")
else:
    print(f"{player2} will start first.")
    

winner = game_play(player1, player2)

print(f"Congratulations {winner}! You are the winner!")
print(f"The dice was rolled {counter} times during the game.")
