import random
import statistics 
roll_list = []
def roll_dice(n):
    roll_list = []
    while n > 0:
        roll = random.randint(1,6)
        print(roll)
        n = n -1
        roll_list.append(roll)
    return roll_list
    




def avg_roll(roll_list, n):
    total = sum(roll_list)
    avg_roll = total/n
    return avg_roll

def most_roll(roll_list):
    roll_mode = statistics.mode(roll_list)
    return roll_mode

def min_roll(roll_list):
    return

n = int(input("How many times should the dice be rolled?\n"))

roll_list = (roll_dice(n))

print("Your average roll was: " + str(round(avg_roll(roll_list, n), 2)))

print("The most common roll was: " + str(most_roll(roll_list)))
