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