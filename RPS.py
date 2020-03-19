from random import randint


def results():

    # Define scoring variables
    computer = 0
    human = 0
    number = 0

    # Create a loop to continue the game until the user inputs a break value
    while number < number + 1:

        # The computers decision
        choice = ["Rock", "Paper", "Scissors"]
        decision = randint(0, 2)
        answer = choice[decision]

        # The users decision
        user = input("Rock Paper or Scissors?: ")
        print("The computer chose: ", answer)

        # Create variables to asses win conditions
        draw = "It's a draw!"
        win = "You Win!"
        lose = "You Lose!"

        # Decide if user won or lost
        if user == answer:
            result = draw
        elif user == "Paper" and answer == "Rock":
            result = win
        elif user == "Scissors" and answer == "Paper":
            result = win
        elif user == "Rock" and answer == "Scissors":
            result = win
        else:
            result = lose
        print(result)

        # Increment the scores and print the current results
        if result == win:
            human = human + 1
            print("The score is now:")
            print("human - ", human)
            print("computer - ", computer)
        elif result == lose:
            computer = computer + 1
            print("The score is now:")
            print("human - ", human)
            print("computer - ", computer)
        else:
            print("The score is now:")
            print("human - ", human)
            print("computer - ", computer)
            
        # Continue or break the loop
        redo = input("Would you like to play again?: ")
        if redo != "y":
            break


# Call the function
results()


