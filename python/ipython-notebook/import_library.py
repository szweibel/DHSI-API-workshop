# Import the "random" library so we can use its functions
import random

print('Random number from 1 to 100: ')
print(random.randint(1,100))

print('')

def roll_dice(number_of_dice):
    for x in range(0,number_of_dice):
        print(random.randint(1,6))

print('Roll dice:')        
roll_dice(5)
