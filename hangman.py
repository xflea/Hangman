man_array = ['''
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

import random, os

def clean_screen():  
    if os.name == 'nt': 
        os.system('cls') 
    else: 
        os.system('clear')

def write_rules():
	print('The word/sentence has been extracted, try to guess it...\n')
	print('RULES:')
	print('- You have ' + str(max_errors) + ' errors available;')
	print('- You can try to guess the word/sentence by typing it, but if you get it wrong, you lose!')

# I try to open the dictionary file, if I can't find it, I create one with standards words/senteces 
try:
  dictionary_file = open("dictionary.txt", "r")
  print("Dictionary has been found! Loading...\n")
except:
  dictionary_file = open("dictionary.txt", "w")
  words = ['dog','cat','hello world']
  for p in words:
    dictionary_file.write(p + "\n")
  print("Dictionary file not found, I made it one for you, add many words/sentences, one per line!\n")

dictionary_file = open("dictionary.txt", "r")
words = dictionary_file.readlines()
dictionary_file.close()

# inizializzo il gioco
letter_tries = []
letter_to_guess = []
guessed = False
current_errors = 0
max_errors = 5

# estraggo la parola
to_guess = str(random.choice(words)[:-1])

# metto le lettere nell'array di quelle da indovinare
for letter in to_guess:
  if letter not in letter_to_guess:
    if letter != ' ':
      letter_to_guess.append(letter)

input("Game is about to start, press ENTER to begin ")

# inizia il ciclo del gioco
while guessed == False:

  write_rules()
  print(man_array[current_errors] + "\n\n")

  for char in to_guess:
    if char in letter_tries:
      print(char, end = " ")
    elif char == ' ':
      print(" ", end = " ")
    elif char not in letter_tries:
      print("_", end = " ")

  print("\n\n")

  print("You already tried: ")
  print(letter_tries)
  print('\n')
  letter_input = str(input("Write the letter/sentence > ")).lower()

  # l'utente può provare a indovinare subito la parola, ma se sbaglia perde direttamente
  if letter_input == to_guess and len(letter_input) > 1:
  	guessed = True
  elif letter_input != to_guess and len(letter_input) > 1:
  	current_errors = 6
  	break

  # inserisco la letter tentata nella lista, sempre se non c'è
  if letter_input not in letter_tries:
  	letter_tries.append(letter_input)

  # controllo se non ha preso nessuna letter e il conteggio degli current_errors
  if letter_input not in to_guess:
    current_errors += 1
    if current_errors > max_errors:
        current_errors = 6
        break

  # rimuovo la letter dalla lista di quelle da indovinare e controllo se la lista è vuota, se lo è il giocatore ha vinto
  for char in letter_to_guess:
  	if letter_input == char:
  		letter_to_guess.remove(char)
  	if not letter_to_guess:
  		guessed = True

  clean_screen()

clean_screen()

write_rules()
print(man_array[current_errors])

if guessed:
  print("You won! The solution was: " + to_guess)
else:
  print("You lose... The solution was: " + to_guess)