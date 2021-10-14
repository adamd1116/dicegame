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

#def rolldice():
#   return random.randint(1,6)

if pt == 1:

    while round <= 5:
        
        if player1Score or player2Score < 0:
            if player1Score < 0:
                print("Player 2 wins! Player 1's score went under 0")
            elif player2Score < 0:
                print("Player 1 wins! Player 2's score went under 0")
            elif player2Score and player1Score < 0:
                print("Both players' scores went beneath 0, no one wins!")

        rollforp1 = input("\n\tPlayer 1, Enter Y to roll: ")
        if rollforp1.upper() == 'Y':
            roll1forplayer1 = random.randint(1,6)
            roll2forplayer1 = random.randint(1,6)
            rolltotal = roll1forplayer1 + roll2forplayer1
            
            if rolltotal % 2 == 0:
                print("Even number! You get 10 free points")
                player1Score += (rolltotal+10)
                print(f"Player 1's total: {player1Score}")
            
            elif rolltotal % 2 != 0:
                print("You rolled an even number, you lose 5 points!")
                player1Score += (rolltotal - 5)
            
            if roll1forplayer1== roll2forplayer1:
                print("You rolled a double! You now get an extra roll of one dice!")
                extraroll = random.randint(1,6)
        
        rollforp2 = input("\n\tPlayer 1, Enter Y to roll: ")
        if rollforp2.upper() == 'Y':
            roll1forplayer2 = random.randint(1,6)
            roll2forplayer2 = random.randint(1,6)
            rolltotal2 = roll1forplayer2 + roll2forplayer2
            
            if rolltotal2 % 2 == 0:
                print("Even number! You get 10 free points")
                player1Score += (rolltotal2+10)
                print(f"Player 1's total: {player1Score}")
            
            elif rolltotal2 % 2 != 0:
                print("You rolled an even number, you lose 5 points!")
                player1Score += (rolltotal2 - 5)
            
            if roll1forplayer2== roll2forplayer2:
                print("You rolled a double! You now get an extra roll of one dice!")
                extraroll = random.randint(1,6)