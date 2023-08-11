### Setup Section ###
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):
  # Loop through each index/position
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if(letter in actual):
        

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word
      if(letter == actual[index]):
      # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index
      else:

        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter,True,False)
    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
        printColorfulLetter(letter,False,False)
      
    print(Style.RESET_ALL + " ", end="")

# Custom Get Six Letter Word Function
def getSixLetterWord():
  # Ask the user to enter a six letter word
  word_input = ""

  # Go through each letter in the word
  while(len(word_input) != 6):
    # Reprompt for a new word
    word_input = input("Enter a six letter word: ")
  #return the user's input
  return word_input

### Main Program ###

#Put ASCI Art Here
print(r"""
.  .   .  .         .   .--. .          .
 \  \ /  /          |   |   )|          |
  \  \  /.-. .--..-.|   |--' | .-.  .  .|
   \/ \/(   )|  (   |   |    |(   ) |  |'
    ' '  `-' '   `-'`-  '    `-`-'`-`--|o
                                       ; 
                                    `-'  
""")
print()

#Display a welcome message and friendly title
print("Welcome to Word Play!")
print("===================")
print()
print("You have six chances to get the word correct")
print()
print("The word is SIX CHARACTERS long! Please do NOT enter more or less")
print()
print("If a letter is in the correct place, it will be green")
print()
print("If a letter is in the word but NOT in the correct place, it will be yellow")
print()
print("If the letter is NOT in the word, it will be red")
print()

#Empty string, counter, and secret word
actual= "avatar"
count= 0
myWord= ""

#Repeats the player's turn until they either run out of tries or guess the word correctly
while(myWord != actual and count<6):
  myWord= getSixLetterWord()
  count+= 1
  
  #On each turn, takes in a word, and shows them how accurate it was
  printGuessAccuracy(myWord,actual)
  print()
  #When they've finished, tells them if they won or lost
  if(myWord == actual):
    print("You Win!")
  
  else:
    if(count==6):
      print("You lose!")