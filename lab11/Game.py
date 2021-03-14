import random

#Menu
def tryAgain():
        answer = input("\n====================\nDo you want to play another game? Y/N ")

        #Invalid input check
        while answer not in ('Y', 'y', 'N', 'n'):
            print("That is not valid input. Please type either Y or N.")
            answer = input("\nDo you want to play again? Y/N ")

        #User says Y
        if answer == "Y" or answer == "y":
            choice = int(input("\nWhich game would like you to play? Choose 1 or 2.\n1) Roll of the Dice\n2) Guess the Number\n\nChoice: "))

            #Invalid input check
            while choice not in (1, 2):
                print("That is not a valid choice. Please type either 1 or 2.\n")
                choice = int(input("Which game would like you to play? Choose 1 or 2.\n1) Roll of the Dice\n2) Guess the Number\n\nChoice: "))

            if choice == 1:
                #Game Choice 1
                diceRoll()
            else:
                #Game Choice 2
                guessNum()
        
        #User says N
        else:
            print("\nThank you for playing!")


#Guessing Game - Roll of the Dice
def diceRoll():
        print("\n====================\nWelcome to the Roll of the Dice. You will have to guess a number from 1 to 6.")
        
        #Ask the user for # of rolls
        rolls = int(input("How many rolls do you want to play? "))

        points = 0

        #For each roll, the user guesses a random # between 1-6
        #Give the user +6 points if they are right
        #Give the user -1 point if they are wrong
    
        while rolls > 0:
            x = random.randint(1,6)
            #print ("Correct answer: ", x) Check
            guess = int(input("\nYour guess: "))

            #Optional: Invalid input check (Guess should be 1-6)
            
            print("\nCorrect answer: ", x)

            if guess == x:
                points += 6
                print("Great job! +6 points")
            else:
                points -= 1
                print("Awww! Try again? -1 point")
            rolls -= 1

        #Print the final score after all the rolls are played
        print("\nYour final score: ", points)

        #Back to menu
        tryAgain()

#Guessing Game - Guess the Number
def guessNum():
    print("\n====================\nWelcome to Guess the Number.")
    
    answer = random.randint(1,100)

    rolls = 1
    print("Guess an integer from 1 to 100. You will have 5 tries. Go!")


    while rolls < 6:
        guess = int(input("Guess " + str(rolls) + ": "))

        #Optional: Invalid input check (Guess should be 1-100)

        if guess == answer:
            print("Great job, you guessed it!")
            rolls = 6
        elif guess > answer:
            print("Your guess is greater than the answer.")
        else:
            print("Your guess is lower than the answer.")

        rolls += 1

    #Back to menu
    tryAgain()

#Start program
choice = int(input("\nWhich game would like you to play? Choose 1 or 2.\n1) Roll of the Dice\n2) Guess the Number\n3) EXIT\n\nChoice: "))

while choice not in (1, 2, 3):
        print("That is not valid input. Please type either 1, 2 or 3.")
        choice = int(input("\nWhich game would like you to play? Choose 1 or 2.\n1) Roll of the Dice\n2) Guess the Number\n3) EXIT\n\nChoice: "))

if choice == 1:
    #Game Choice 1
    diceRoll()
elif choice == 2:
    #Game Choice 2
    guessNum()
    #End program
else:
    print("Have a nice day!")
