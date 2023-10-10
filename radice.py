import random
def roll_dice():
    """Returns nested tuple with two values (two dice) and sum of roll"""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    return (dice1, dice2), dice1+dice2

if __name__ == "__main__":
    print(roll_dice())