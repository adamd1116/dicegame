#dice game
#If you use this, make sure to get a password.txt file which contains your password in the same directory
import random

password = input("Enter your password here: ")
pt = 0
round = 0
player1Score = 0
player2Score = 0

def roll():
    return random.randint(1,6)

with open('password.txt', 'r') as f:
    if password != f.read():
        print("Incorrect password, please try again")
        pt = 0
    else:
        print("Correct password")
        pt = 1

if pt == 1:

    while round < 5:

        round += 1
        print("\n\t----------------------")
        print(f"\tRound {round}")
        print("\t----------------------")

        rollforp1 = input("\n\tPlayer 1, Enter Y to roll: ")
        if rollforp1.upper() == 'Y':
            roll1forplayer1 = roll()
            roll2forplayer1 = roll()
            rolltotal = roll1forplayer1 + roll2forplayer1
            
            if rolltotal % 2 == 0:
                print("\n\tEven number! You get 10 free points")
                player1Score += (rolltotal+10)
                print(f"\tPlayer 1's total: {player1Score}")
            
            elif rolltotal % 2 != 0:
                print("\n\tOdd number! You lose 5 points!")
                player1Score += (rolltotal - 5)
                print(f"\tPlayer 1's total: {player1Score}")
                if player1Score < 0:
                    print("\n\tPlayer 2 wins, player 1's score is less than 0")
                    sS = 1
                    break
            
            if roll1forplayer1== roll2forplayer1:
                print("\n\tYou rolled a double! You now get an extra roll of one dice!")
                extraroll = roll()
                player1Score += extraroll
                print(f"\tPlayer 1's total: {player1Score}")
        else:
            print("\n\tInvalid input, try again next time")
            sS = 1
            break

        print("\n\t----------------------")
        rollforp2 = input("\n\tPlayer 2, Enter Y to roll: ")
        if rollforp2.upper() == 'Y':
            roll1forplayer2 = roll()
            roll2forplayer2 = roll()
            rolltotal2 = roll1forplayer2 + roll2forplayer2
            
            if rolltotal2 % 2 == 0:
                print("\n\tEven number! You get 10 free points")
                player2Score += rolltotal2 + 10
                print(f"\tPlayer 2's total: {player2Score}")
            
            elif rolltotal2 % 2 != 0:
                print("\n\tOdd number! You lose 5 points")
                player2Score += rolltotal2 - 5
                print(f"\tPlayer 2's total: {player2Score}")
                if player2Score < 0:
                    print("\n\tPlayer 1 wins, player 2's score is less than 0")
                    sS = 1
                    break
            
            if roll1forplayer2== roll2forplayer2:
                print("\n\tYou rolled a double! You now get an extra roll of one dice!")
                extraroll2 = roll()
                player2Score += extraroll2
                print(f"\tPlayer 2's total: {player2Score}")
        else:
            print("\n\tInvalid input, try again next time")
            sS = 1
            break

if round == 5:
    print("\n\t----------------------")
    if player1Score > player2Score:
        print(f"\n\tPlayer 1 wins with a score of {player1Score}")
        sS = 1
    elif player2Score > player1Score:
        print(f"\n\tPlayer 2 wins with a score of {player2Score}")
        sS = 1
    elif player1Score == player2Score:
        print("\n\tBoth players have the same score, you will each roll\n\tone dice until someone gets a higher number!")
        while True:
            player1SD = roll()
            player2SD = roll()

            print(f"\n\tPlayer 1 roll: {player1SD}")
            print(f"\tPlayer 2 roll: {player2SD}")

            if player1SD > player2SD:
                print("\n\tPlayer 1 wins")
                sS = 1
                player1Score += 10
                break
            elif player2SD > player1SD:
                print("\n\tPlayer 2 wins")
                sS = 1
                player2Score += 100
                break
            else:
                print("\n\tDraw, keep playing")

if sS == 1 and pt == 1:
    with open('scores.txt', 'a') as fs:
        fs.write("------------------------\n")
        fs.write(f"Player 1 score: {player1Score}")
        fs.write(f"\nPlayer 2 score: {player2Score}\n")

        if player1Score > player2Score:
            fs.write("\n\tPlayer 1 won!") 
        elif player1Score == player2Score:
            fs.write("\n\tDraw!")
        else:
            fs.write("\n\tPlayer 2 won!")

        fs.write("\n------------------------\n")