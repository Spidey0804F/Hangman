#Potatoboy9999
#Hangman
#5/18/20

import os, sys, random

#Main Menu
def Menu():
    #Clear console
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    while True:
        print("Welcome to HANGMAN\n")
        #Print completed hangman
        PrintHangMan(0)

        #Give user options
        print("\nMENU:")
        print("1. PLay With Random Word")
        print("2. Play With Custom Word")
        print("3. How To Play")
        print("4. Quit")
    
        #Get sser input
        userChoice = input("\nSelect An Option: ")

        #Checks if user choose an option
        if userChoice in ("1", "2", "3", "4"):
            #Clear console
            os.system('cls' if os.name == 'nt' else "printf '\033c'")
            if userChoice == "1":
                PlayRandom()
            elif userChoice == "2":
                PlayCustom()
            elif userChoice == "3":
                HowToPlay()
            else:
                #Close console
                sys.exit()
            break
        else:
            #Clear console
            os.system('cls' if os.name == 'nt' else "printf '\033c'")

def PlayRandom():
    #Start the hangman game with a random word taken from list
    RunGame(random.choice(wordList).upper())

def PlayCustom():
    #Ask user for word to use then start game with it
    RunGame(input("Enter The Word/Phrase To Guess: ").upper())

def HowToPlay():
    #Clear console
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    #Print game instructions
    print("How To Play:")
    print("GOAL: Guess The Secret Word\n")
    print("Try to guess the secret word by guessing 1 letter at a time.")
    print("If you guess a letter in the word it will appear.")
    print("If your guess isn't in the word you will lose on of your 6 lives.")
    print("When the you run out of lives and the hangman is complete,")
    print("YOU LOSE.")

    #Return to menu when user presses enter
    input("\nPress Enter To Return To Menu...")
    Menu()

def RunGame(word):
    #Clear console
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    #Sets users lives
    health = 6

    #Initialize guessed letter array
    guessedLetters = []

    #remove spaces from word/phrase
    wordWithoutSpace = word.replace(" ","")

    while True:
        #Prints hangman with current health
        PrintHangMan(health)

        #For each letter in the word/phrase
        for char in word:
            #if the letter is a space
            if char == " ":
                #add a space
                print("   ", end = "")
            #If the letter has been guessed, show letter
            elif char in guessedLetters:
               print(char.upper() + " ", end = "")
            #If the letter isnt a space and hasnt been guessed, show a _
            else:
               print("_ ", end = "")

        #Prints the letters that have been guessed
        print("\n\nGuessed Letters: ")
        print(*guessedLetters)

        #Asks user for their guess and puts it in upper case. If they didnt enter anything an IndexError occers and guess it set to a space
        try:
            guess = input("Guess: ")[0].upper()
        except IndexError:
            guess = " "

        #If the guess hasnt been guessed
        if guess and guess not in guessedLetters:
            #Add it to guessed letters
            guessedLetters.append(guess)

            #If the letter isn't in the word, lose a life
            if guess not in wordWithoutSpace:
                health -= 1

        #If the user has no lives left, call the Lose function and break out of loop
        if health <= 0:
            Lose(word, health)
            break

        #If the guessed letters array contains all the letters in the word, call the Win function and break out of the loop
        if all(char in guessedLetters for char in wordWithoutSpace):
            Win(word, health)
            break

        #Clear console
        os.system('cls' if os.name == 'nt' else "printf '\033c'")

def Lose(word, health):
    #Clears console
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    #Prints hangman with amount of health user had
    PrintHangMan(health)

    #Prints lose message and the correct word
    print("\nYOU LOSE. The word was: " + word + ". Better luck next time!")

    #Returns to menu when user presses enter
    input("\nPress Enter To Return To Menu...")
    Menu()

def Win(word, health):
    #Clears console
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    #Prints hangman with amount of health user had
    PrintHangMan(health)

    #Prints win message and correct word
    print("\nYOU WIN!!! You correctly guessed: " + word + ". Awesome Job!")

    #Returns to menu when enter is pressed
    input("\nPress Enter To Return To Menu...")
    Menu()

def PrintHangMan(health):
    #Prints hangman depending on amount of health

    print("_____   ")
    print("|   |   ")

    if health > 5:
        print("|       ")
    else:
        print("|   O   ")

    if health > 4:
        print("|       ")
    elif health > 3:
        print("|   |   ")
    elif health > 2:
        print("|   |\  ")
    else:
        print("|  /|\  ")

    if health > 1:
        print("|       ")
    elif health > 0:
        print("|    \  ")
    else:
        print("|  / \  ")

wordList = [
    "cat",
    "dog", 
    "apple",
    "president",
    "water",
    "graphics card",
    "computer science",
    "canada",
    "space whale",
    "laser shark",
    "speed boat",
    "the sun is yellow",
    "pirate ship",
    "hangman",
    "look outside",
    "central processing unit",
    "calculator",
    "bricks are red"
    ]

#Calls main menu when program is ran
Menu()