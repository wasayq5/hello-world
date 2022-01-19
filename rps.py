import random
def play_again(user_win, user_score, comp_score):
    """
    Inputs: user_win, user_score, comp_score
    Asks the user if they want to play again. 
    If the user chooses to play again, checks user_win to see if the user won or lost the last match or if it was a draw.
    Calls the rock_paper_scissors function, with user_score and comp_score having different values based on value of user_win
    """
    
    print("  ")
    play_again = input("Do you want to play again? type 'yes' or 'no': ")
    possible_choices = ["yes", "no"]
    while play_again not in possible_choices:
        print("Invalid choice, only 'yes' or 'no' are acceptable inputs!")
        play_again = input("Do you want to play again? type 'yes' or 'no': ")

    if play_again == "yes":
        if user_win == "win":
            rock_paper_scissors(user_score+1, comp_score)
        elif user_win == "lose":
            rock_paper_scissors(user_score, comp_score+1)
        else:
            rock_paper_scissors(user_score, comp_score)
    if play_again == "no":
        print("Thanks for playing!")

def rock_paper_scissors(user_score=0, comp_score=0):
    """
    Inputs: user_score and comp_score, both initially set to 0
    Asks the user what they want to play and gets the computer to make a random play. 
    Then, the user_win variable stores whether the user won, lost or if the match was a draw.
    Passes the variables user_win, user_score, and comp_score to the play_again function
    """

    print("----------------------------------------------------")
    print("Hello! Welcome to Wasay's rock-paper-scissors game!")
    print("Currently, the user has %d win(s) and the computer has %d win(s)" % (user_score, comp_score))

    print("    ")

    possible_plays = ['rock', 'paper', 'scissors']
    user_play = input("Enter your play (rock, paper, or scissors): ")
    while user_play not in possible_plays:
        print("Invalid choice! play rock, paper, or scissors")
        user_play = input("Enter your play (rock, paper, or scissors): ")

    comp_play = random.choice(possible_plays)

    print("   ")
    
    print("You played %s, and the computer played %s" % (user_play, comp_play))

    if user_play == comp_play:
        print("Both you and the computer had the same play! It's a draw")
        user_win = 'draw'
    elif user_play == 'rock' and comp_play == 'scissors':
        print("You won!")
        user_win = 'win'
    elif user_play == 'paper' and comp_play == 'rock':
        print("You won!")
        user_win = 'win'
    elif user_play == 'scissors' and comp_play == 'paper':
        print("You won!")
        user_win = 'win'
    else:
        print("The computer won!")
        user_win = 'lose'

    play_again(user_win, user_score, comp_score)


rock_paper_scissors()