#README
#I referred to another code for the visuals because its brilliant
#https://inventwithpython.com/bigbookpython/project4.html
#Other than that, I did most of the game logic myself

import random

heart   = chr(9829) # Character 9829 is '♥'.
diamond = chr(9830) # Character 9830 is '♦'.
spade   = chr(9824) # Character 9824 is '♠'.
club    = chr(9827) # Character 9827 is '♣'.
backside = 'backside'
cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

def getStartingHand(cards):
    # card1.choice(cards)??
    card1 = random.randrange(0,13)
    card2 = random.randrange(0,13)

    card1 = cards[card1]
    card2 = cards[card2]

    hands = [card1, card2]

    return hands

def getAnotherCard(cards):
    card = random.randrange(0,13)
    card = cards[card]

    return card

def getValues(hands):
    value = 0

    for hand in hands:
        if hand == 'A':
            value += 11
        elif hand in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(hand)

    return value

def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False."""
    print()
    if showDealerHand:
        print('DEALER:', getValues(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        displayCards([backside] + dealerHand[1:])

    # Show the player's cards:
    print('YOUR HAND:', getValues(playerHand))
    displayCards(playerHand)

def displayCards(cards):
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', '']  # The text to display on each row.
 
    for card in cards:
        rows[0] += ' ___  '  # Print the top line of the card.
        if card == backside:
        # Print a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
        # Print the card's front:
            suits = [heart, diamond, spade, club]
            suit = random.choice(suits)

            rank = card
            rows[1] += '|{} | '.format(str(rank).ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(str(rank).rjust(2, '_'))

        # Print each row on the screen:
    for row in rows:
        print(row)

print('''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/ 
''')

#TODO: READ HIGH SCORES

money = 1000

while True:
    if money <= 0:
        print('\nSORRY, YOU JUST WENT BROKE. ')

    choice = input("\nWould you like to play again? ( y for yes, n for no )\n").lower()
    if choice == 'n':
        print()
        break
    elif choice == 'y' and money <= 0:
        money == 1000
    elif choice != 'n' and choice != 'y':
        print('\nIt seems you mistyped, but too lazy to add the retry step so imma make you play again.')
    
    print("\n\nMONEY: $" + str(money))

    while True:
        wager = input("\nHow much would you like to bet? ( Enter an amount within your money range or QUIT )\n$").lower()

        if wager == 'quit':
            print()
            break
        elif int(wager) > money or int(wager) < 0:
            print('Please enter any amount between 0 and ' + str(money + 1) + ' or QUIT')
        else:
            break
    
    if wager == 'quit':
            print()
            break

    print("\nBET: $" + wager)

    yourHands = getStartingHand(cards)
    yourValue = getValues(yourHands)

    compHands = getStartingHand(cards)
    compValue = getValues(compHands)

    while True:

        #CHECK FOR 21
        if compValue == 21 or yourValue > 21:
            displayHands(yourHands, compHands, True)

            money -= int(wager)
            print('\n\nYOU LOSE!!!')
            break
        elif yourValue == 21 or compValue > 21:
            displayHands(yourHands, compHands, True)

            money += int(wager)
            print('\n\nYOU WON!!!')
            break
        else:
            displayHands(yourHands, compHands, False)
            choice = input("\nDraw another card? ( y for yes, n for no, or QUIT )\n").lower()

            if choice == 'y':

                plusCard = getAnotherCard(cards)
                yourHands.append(plusCard)
                yourValue = getValues(yourHands)

                compChoice = random.randrange(1,3)
                if compChoice == 1:
                    plusCard = getAnotherCard(cards)
                    compHands.append(plusCard)
                    compValue = getValues(compHands)

            elif choice == 'n':

                compChoice = random.randrange(1,3)
                if compChoice == 1:
                    plusCard = getAnotherCard(cards)
                    compHands.append(plusCard)
                    compValue = getValues(compHands)

            elif choice == 'quit':
                break
        
    if choice == 'quit':
        print()
        break

print('\nGAME OVER\nThanks for playing!')