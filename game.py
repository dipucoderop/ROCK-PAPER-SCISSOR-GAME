import random
C=str(input("ENTER YOUR USERNAME SIR:"))
print("WELCOME",C)
h=str(input("TYPE LAL SALAM TO START THE GAME:"))
M=0
if h.upper()=="LAL SALAM":
    print("OK! LETS START THE GAME")
    print("YOU HAVE TO SCORE 69 TO WIN THE GAME")
    v=int(input("ENTER HOW MANY ROUNDS DO YOU WANT:"))
    b=0
    x=69/v
    print("you will be awarded", x ,"each time you win")
    print("YOU HAVE TO TYPE ROCK,PAPER,SCISSOR OR ROPE AND IF YOU GIVE INVALID INPUT MORE THAN ONE TIME YOU WILL BE DISQUALIFIED")
    print()
    for i in range(v):
        n=["ROCK","PAPER","SCISSOR","ROPE"]
        d=random.choice(["ROCK","PAPER","SCISSOR","ROPE"])
        e=str(input("YOU:"))
        if e.upper() in n:
           print()
           if e.upper() == d:
               print("CONGRATS! YOU WON THIS ROUND")
               b+=x
           else:
                print("Regrets you lost this round")
           print()
        else:
            print("DEAR",C,"PLEASE GIVE VALID INPUT AND IF YOU AGAIN GIVE WRONG INPUT YOU WILL BE DISQUALIFIED")
            M+=1
            print( )
            if M>1:
              print("YOU ARE DISQUALIFIED")
              break
            else:
                continue
    if b>=69:
        print("YOU WON ")
    else:
        print("YOU LOST AND YOUR SCORE IS:",b)
else:
    print("JETA BOLCHI OTA KOR JHATU")