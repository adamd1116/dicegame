#dice game
import random

password = input("Enter your password here: ")
pt = 0
round = 1
player1Score = 0
player2Score = 0

with open('password.txt', 'r') as f:
    if password != f.read():
        print("Incorrect password, please try again")
        pt = 0
    else:
        print("Correct password")
        pt = 1

def rolldice():
    return random.randint(1,6)

def playerRollDice(player,player1Sc,player2Sc):
    Dresult1 = rolldice()
    Dresult2 = rolldice()
                
    if Dresult1 == Dresult2 and player == 1:
        player1Sc += Dresult1+Dresult2
        print(f"You got {Dresult1} and {Dresult2}, you get extra or less points if your 2 dice are even or odd")
        if player1Sc % 2 == 0:
            player1Sc += 10
        else:
            player1Sc -= 5
        player1Sc += rolldice()

    elif Dresult1 != Dresult1 and player == 1:
        player1Sc += Dresult1+Dresult2
        print(f"You got {Dresult1} and {Dresult2}, you get extra or less points if your 2 dice are even or odd")
        if player1Score % 2 == 0:
            player1Sc += 10
        else:
            player1Sc -= 5

    if Dresult1 == Dresult2 and player == 2:
        player2Sc += Dresult1+Dresult2
        print(f"You got {Dresult1} and {Dresult2}, you get extra or less points if your 2 dice are even or odd")
        if player2Sc % 2 == 0:
            player2Sc += 10
        else:
            player2Sc -= 5
        player2Sc += rolldice()

    elif Dresult1 != Dresult1 and player == 2:
        player2Sc += Dresult1+Dresult2
        print(f"You got {Dresult1} and {Dresult2}, you get extra or less points if your 2 dice are even or odd")
        if player2Sc % 2 == 0:
            player2Sc += 10
        else:
            player2Sc -= 5

if pt == 1:
    for i in range(1,6):
        
    
        player1Roll = input("Player 1, enter roll to roll: ")
        player2Roll = input("Player 2, enter roll to roll: ")

        if player1Roll.lower() and player2Roll.lower() == 'roll':

            playerRollDice(1,player1Score,0)
            playerRollDice(2,0,player2Score)
        
        else:
            print("error")
            print(player1Roll)
            print(player2Roll)
            
        if i == 5:
            a = 1

if player1Score == player2Score and a==1:
    while player1Score == player2Score:
        print("Both players have the same score, you will now play until")