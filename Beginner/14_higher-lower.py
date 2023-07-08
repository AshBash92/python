import random
import os
import sys
sys.path.append('../')

from Extras._14_game_data import data ## Had to rename from 14_game-data because it created an error

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

print(logo)

points = 0
stillPlaying = True


while stillPlaying:

    personA = random.choice(data)
    personB = random.choice(data)

    print('\nWho has more followers?\n')
    print('A: ' + personA['name'] + ', ' + personA['description'] + ' from ' + personA['country'])
    print(vs)
    print('\nB: ' + personB['name'] + ', ' + personB['description'] + ' from ' + personB['country'])

    personA = personA['follower_count']
    personB = personB['follower_count']

    winnerA = personA > personB

    while True:
        guess = input("\nChoose between \'A\' and \'B\'\n").lower()

        if (guess == 'a' and winnerA) or (guess == 'b' and winnerA == False):
            os.system('cls')
            points += 1
            print('\nNice, you got it right!\nPOINTS: ' + str(points))
            break
        elif guess != 'a' and guess != 'b':
            print('\nINVALID INPUT, PLEASE TRY AGAIN.')
        else:
            print('\nSorry, you got it wrong.')
            stillPlaying = False
            break

print('\nGAME OVER.\nThanks for playing!')