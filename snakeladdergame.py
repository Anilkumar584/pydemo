import random

# Snakes and Ladders positions
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}


# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)


# Function to move player on the board
def move_player(position):
    dice_roll = roll_dice()
    print(f"Dice rolled: {dice_roll}")
    position += dice_roll

    if position in snakes:
        print(f"Oops! Bitten by a snake at {position}. Sliding down to {snakes[position]}")
        position = snakes[position]
    elif position in ladders:
        print(f"Yay! Climbed a ladder at {position}. Moving up to {ladders[position]}")
        position = ladders[position]

    return position


# Main game function
def play_game():
    player_position = 0

    while player_position < 100:
        input("Press Enter to roll the dice...")
        player_position = move_player(player_position)
        print(f"Player is now on position {player_position}")

        if player_position >= 100:
            print("Congratulations! You won the game!")


# Start the game
if __name__ == "__main__":
    play_game()
