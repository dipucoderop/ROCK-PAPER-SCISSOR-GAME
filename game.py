import random
C=str(input("ENTER YOUR USERNAME SIR:"))
print("WELCOME",C)
h=str(input("TYPE LAL SALAM TO START THE GAME:"))
if h.upper()=="LAL SALAM":
    print("OK! LETS START THE GAME")
    print("YOU HAVE TO SCORE 69 TO WIN THE GAME")
    v=int(input("ENTER HOW MANY ROUNDS DO YOU WANT:"))
    b=0
    x=69/v
    print("you will be awarded", x ,"each time you win")
    print("YOU HAVE TYPE ROCK,PAPER,SCISSOR OR ROPE")
    print()
    for i in range(v):
        d=random.choice(["ROCK","PAPER","SCISSOR","ROPE"])
        e=str(input("YOU:"))
        print()
        print("COMPUTER:",d)
        if e.upper() == d:
            print("CONGRATS! YOU WON THIS ROUND")
            b+=x
        else:
            print("Regrets you lost this round")
        print()
    if b>=69:
        print("YOU WON ")
    else:
        print("YOU LOST AND YOUR SCORE IS:",b)
else:
    print("JETA BOLCHI OTA KOR JHATU")