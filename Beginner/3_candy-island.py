def valid():
    print("\nPLEASE ENTER A VALID ANSWER.")

def play_again():
    invalid = True

    while invalid == True:
        invalid = False
        print("\nWould you like to try again? (y/n): ")
        x = input().lower()

        if x == "n":
            loop = False
        elif x == "y":
            loop = True
            print("\n= = = = = = = = = = = = = = = = = = = = = = = = =")
        else:
            print("\nPLEASE ENTER A VALID ANSWER.")
            invalid = True
    
    return loop

#CREDIT: GAME OVER ASCII ART
#https://emojicombos.com/game-over-ascii-art
def game_over(choice):
    print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⢀⣤⣤⣤⣶⣶⣷⣤⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⣶⣶⣶⠀⠀⠀⠀⣠⣾⣿⣿⡇⠀⣿⣿⣿⣿⠿⠛⠉⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⢀⣿⣿⣶⡀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡄⠀⢀⣴⣿⣿⣿⣿⠁⢸⣿⣿⣿⣀⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣼⣿⣿⣿⣧⠀⠀⠀⠀⢰⣿⣿⣿⣿⣇⣠⣿⣿⣿⣿⣿⡏⢠⣿⣿⣿⣿⣿⡿⠗⠂⠀⠀
⠀⠀⠀⣰⣾⣿⣿⠟⠛⠉⠉⠉⠉⠋⠀⠀⠀⣰⣿⣿⣿⣿⣿⣇⣠⣤⣤⣿⣿⣿⢿⣿⣿⣿⣿⢿⣿⣿⡿⠀⣼⣿⣿⡟⠉⠁⢀⣀⡄⠀⠀
⠀⢀⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣴⣿⣿⣿⣿⡿⣿⣿⣿⡏⠈⢿⣿⣿⠏⣾⣿⣿⠃⢠⣿⣿⣿⣶⣶⣿⣿⣿⡷⠦⠀
⢠⣾⣿⡿⠀⠀⠀⣀⣠⣴⣶⣿⣿⡷⠀⣠⣿⣿⣿⣿⡿⠟⣿⣿⣿⣠⣿⣿⣿⠀⠀⠀⠀⠁⢸⣿⣿⡏⠀⣼⣿⣿⣿⠿⠛⠛⠉⠀⠀⠀⠀
⢸⣿⣿⠣⣴⣾⣿⣿⣿⣿⣿⣿⡿⠃⣰⣿⣿⣿⠋⠁⠀⠀⠸⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠸⠿⠿⠀⠀⠛⠛⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⣿⣆⣉⣻⣭⣿⣿⣿⡿⠋⠀⠀⢿⣿⡿⠁⠀⠀⠀⠀⠀⠹⠟⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀    ⣀⣤⣤⣶⣶⣶⣶⣦⣄⠀⠀
⠀⠙⠿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠈⠁  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⠄⣤⣤⣤⣤⣶⣾⣷⣴⣿⣿⣿⣿⠿⠿⠛⣻⣿⣿⣷⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣄⠀⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠋⢠⣿⣿⣿⠿⠛⠋⠉⠛⣿⣿⣿⠏⢀⣤⣾⣿⣿⡿⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⠓⢹⣿⣿⣷⠀⠀⠀⠀⢀⣶⣿⡿⠁⠀⣾⣿⣿⣟⣠⣤⠀⠀⢸⣿⣿⣿⣾⣿⣿⣿⡟⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⠛⠉⠸⣿⣦⡈⣿⣿⣿⡇⠀⠀⣰⣿⣿⡿⠁⠀⢸⣿⣿⣿⣿⣿⠿⠷⢀⣿⣿⣿⣿⡿⠛⣿⣿⣿⡀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⣿⣿⡿⠋⠀⠀⠀⠀⣿⣿⣧⠘⣿⣿⣿⡀⣼⣿⣿⡟⠀⠀⢀⣿⣿⣿⠋⠁⠀⣀⣀⣼⣿⣿⡟⠁⠀⠀⠘⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⡟⠀⠀⠀⠀⠀⣠⣿⣿⣿⠀⢹⣿⣿⣿⣿⣿⡟⠀⠀⠀⣼⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠸⣿⣿⡆⠀⠀
⠀⠀⠀⠀⢹⣿⣿⣇⠀⠀⢀⣠⣴⣿⣿⣿⡿⠀⠈⣿⣿⣿⣿⡟⠀⠀⠀⢰⣿⣿⣿⠿⠟⠛⠉⠁⠸⢿⡟⠀⠀⠀⠀⠀⠀⠀⠘⠋⠁⠀⠀
⠀⠀⠀⠀⠈⢻⣿⣿⣿⣾⣿⣿⣿⣿⣿⠟⠁⠀⠀⠸⣿⣿⡿⠁⠀⠀⠀⠈⠙⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⠿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')

    print("\n= = = = = = = = = = = = = = = = = = = = = = = = =")
    
    # Define the mapping of choice values to variable names
    mapping = {
        "right": "You fell into a hole.",
        "swim": "You got attacked by a shark.",
        "red": "It's a room full of fire.",
        "blue": "You enter a room of beasts.",
    }

    # Get the value of the choice variable and use it to look up the corresponding value in the mapping
    ending = mapping.get(choice)
    print(ending)


#CREDIT: CANDY ASCII ART
#https://emojicombos.com/candy-ascii-art
print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡴⠶⠞⢛⣉⣉⠉⠉⠉⠻⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠋⢀⣤⠆⠀⠀⠙⠛⠀⠀⠀⠘⠷⣦⠉⠛⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠡⠴⠆⠀⠁⠀⠀⠀⠀⢀⣠⢤⣤⠀⠀⠈⠀⠀⠀⠹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠁⠀⠀⠀⠀⠀⠀⣰⣦⠘⣷⡀⠀⠀⢀⣠⠶⠚⠛⠉⠉⢹⡟⠓⠶⣄⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⠸⡇⢀⡶⠛⠢⡄⠀⠀⠀⠀⠀⡇⠀⠀⠈⢻⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠋⠀⠀⠀⠈⣆⠀⠀⠀⢠⠇⠀⠀⠀⣸⠻⣦⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⡿⠀⠀⠀⠀⣠⠿⠛⠙⠛⠻⢦⣄⡠⠞⠁⠀⢻⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡟⣏⠁⡴⢦⣄⠀⢀⣠⡤⢤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡧⠤⢤⣤⡾⠁⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢾⣦⡇⠀⠈⠉⠉⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠟⠀⠀⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣀⣀⣀⢼⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⡀⢤⣤⣤⣤⣤⣀⠀⠙⠒⠒⠒⢦⠀⠀⠀⢀⡽⠋⠀⠀⣠⡏⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠃⠀⠀⠀⣼⠃
⠀⠀⠀⠀⠀⠀⢀⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢦⣀⢉⡇⢀⠿⠗⠶⠦⠀⠀⢘⣦⣴⠞⠉⠉⠉⠉⣻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢀⣼⠏⠀
⠀⠀⢀⣤⠶⠒⢻⢥⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⣼⠦⠤⠤⠖⠚⠛⠋⣩⠃⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠓⠒⠛⠁⠀⠀
⣴⣖⢛⠅⢠⣰⣿⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⢠⡟⠀⠀⠀⠀⠀⠀⣰⡯⠤⠤⠤⠤⣴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠙⠛⠲⢤⣽⢿⢿⡻⠿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⣸⠃⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⡟⠋⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠧⠶⡟⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⣯⠉⢳⠀⠀⠀⡏⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⣼⠃⠀⠀⠀⠀⣰⠟⠒⠒⠒⠒⣾⠋⠀⠀⠀⠀⠀⠀⠀⣰⠶⢻⡟⠉⠙⠳⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⣧⠞⠀⠀⠀⠈⠛⠛⣷⡀⠀⠀⠀⠀⠀⠀⠀⣼⠃⢀⡿⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⣼⢏⠀⠀⠀⠀⠀⠀⢠⡾⠹⣄⠈⠳⣄⠀⡏⠉⢳⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢷⡀⢠⡤⣄⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⢀⡟⠀⣸⠁⠀⠀⠀⣰⠏⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⢿⣇⣀⣨⠯⣶⣼⣴⠃⣀⣈⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⡹⣄⣼⠇⠀⢠⡾⢷⡄⠀⠀⠀⠀⣸⣁⣠⡟⠀⠀⠀⣰⡟⠛⠉⠉⠉⣹⠏⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠉⢁⡼⠋⡟⣏⣉⡁⢀⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀⠀⠀⠘⣧⠞⠁⠀⠀⠀⢰⡟⠉⣸⠃⠀⠀⣠⡏⠀⠀⠀⠀⣰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⣿⣏⡀⢀⡇⠀⢉⣹⠾⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠦⠤⣶⡿⢿⡓⠶⢤⣀⠀⣼⠃⠀⡟⠀⠀⢠⡿⣀⣀⣀⣀⣰⠏⠀⠀⠀⠀⠀⠀⠀⢀⣴⣟⡵⠋⠀⠈⠙⠛⠓⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⢧⣠⣴⠋⢱⣿⢁⡟⠀⣸⠃⠀⠀⣾⠉⠉⠉⠉⢹⡟⠀⠀⠀⠀⠀⠀⣠⠾⣫⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣈⣫⠾⠶⠟⠁⢸⠁⠀⣿⠀⠀⣼⠃⠀⠀⠀⣰⠟⠀⠀⠀⠀⢀⣴⠟⣡⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠔⢺⠇⠀⠀⣿⣀⠀⠀⣴⠏⠀⠀⠀⣠⡴⠋⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⣼⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠙⠷⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢦⣤⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

print('''\nWelcome to Candy Island.
\nYour mission is to find the hidden stash of candy.
''')

loop = True

# BEGINNING OF GAME LOOP
while loop == True:

    #CROSS ROAD LOOP
    while loop == True:
        print("You're at a cross road. Where do you want to go? Type \"left\" or \"right\".")
        road = input().lower()

        if road == "right":
            game_over(road)
            loop = play_again()
        elif road != "left":
            valid()
        else:
            break
        
    #LAKE LOOP
    while loop == True:
        print("\nYou come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
        lake = input().lower()

        if lake == "swim":
            game_over(lake)
            loop = play_again()
        elif lake == "wait":
            break
        else:
            valid()

    #ISLAND LOOP
    while loop == True:
        print("\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose?")
        color=input().lower()

        if color == "red":
            game_over(color)
            loop = play_again()
        elif color == "blue":
            game_over(color)
            loop = play_again()
        elif color == "yellow":
            print("\nYou found the hidden candy stash! You win!")
            loop == play_again()
        else:
            valid()




print("\nThanks for playing!")
print("\n= = = = = = = = = = = = = = = = = = = = = = = = =")