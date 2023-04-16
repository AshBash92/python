import nltk
from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk import pos_tag

nltk.download('brown')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

import matplotlib.colors as mcl
import random

print('\n\n\nloading...\n\n\n')

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# --- OLDER CODE ---
# This is just for my own reference

# Get the words from the Brown corpus
# brown_words = brown.words()
# stop_words = set(stopwords.words('english'))

# # Compute the frequency distribution
# freq_dist = nltk.FreqDist(w.lower() for w in brown_words if w.isalpha())

# # Get the most common words
# most_common_words = [word for word, freq in freq_dist.most_common()]

# # POS tag the most common words
# tagged_most_common_words = pos_tag(most_common_words)

# # Filter the list to include only nouns
# nouns = [word for word, pos in tagged_most_common_words if pos.startswith('NN') and word.isalpha() and word not in stop_words]
# filter_nouns = [word for word in nouns if len(word) >= 5]
# --- END OF OLDER CODE ---


stop_words = set(stopwords.words('english'))

# Compute the frequency distribution and get the most common words
most_common_words = [word for word, freq in nltk.FreqDist(w.lower() for w in brown.words() if w.isalpha()).most_common()]

# POS tag the most common words and filter the list to include only nouns
nouns = [word for word, pos in pos_tag(most_common_words) if pos.startswith('NN') and word not in stop_words and len(word) >= 5 and len(word) <= 10]

rando = random.randint(0, 14952)
word = nouns[rando]
print("\n" + word) #DELETE

def guess():
  while True:
      choose = input("\nChoose a letter: ").lower()
      if choose.isalpha() == True:
          break
      else:
          print("\nInvalid Selection. Please Try Again.\n")
    
  return choose

def check_guess(choose, word, lines):
  safe = False
  index = word.find(choose)
  
  for index, char in enumerate(word):
    if char == choose:
      lines[index] = choose
      safe = True
    
  print(' '.join(lines))
  return safe


print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')

lives = 0
print(HANGMANPICS[lives])
lines = ["_" for _ in word]
print(' '.join(lines))

keepPlaying = True

while keepPlaying == True:
  choose = guess()
  strike = check_guess(choose, word, lines)

  if strike == False:
    lives += 1
  
  print(HANGMANPICS[lives])

  if lives == 6:
    print("\nLOSER.")
    break
  if not '_' in lines:
    print("\nWINNER")
    break

print("\nGAME OVER")
