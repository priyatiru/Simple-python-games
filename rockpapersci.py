from random import randint

play_options=["Rock","Paper","Scissor"]

#choosing the random play for computer
computer=play_options[randint(0,2)]

player=False  #setting to false initially

#setting true on giving input from player
while player==False:
    player=input("Rock,Paper or Scissor? \n")
    x=0
    y=0
    if player==computer:
        x=0 #for player
        y=0 #for computer
        print("Tie!")
        print("-------------")
        print("Player=",x)
        print("Computer=",y)
        print("-------------")
    elif player=="Rock":
        if computer=="Paper":
            y=y+1
            print("You lose!",computer,"covers",player)
            print("-------------")
            print("Player=",x)
            print("Computer=",y)
            print("-------------")
        else:
            print("You win!",player,"smashes",computer)
            x=x+1
            print("-------------")
            print("Player=",x)
            print("Computer=",y)
            print("-------------")
    elif player=="Paper":
        if computer=="Scissor":
            y=y+1
            print("You lose!",computer,"cuts",player)
            print("-------------")
            print("Player=",x)
            print("Computer=",y)
            print("-------------")
        else:
            print("You win!",player,"covers",computer)
            x=x+1
            print("-------------")
            print("Player=",x)
            print("Computer=",y)
            print("-------------")
    elif player=="Scissor":
        if computer=="Rock":
            y=y+1
            print("You lose!",computer,"smashes",player)
            print("-------------")
            print("Player=",x)
            print("Computer=",y)
            print("-------------")
        else:
            print("You win!",player,"cut",computer)
            x=x+1
            print("-------------")
            print("Player=",x)
            print("Computer=",y)
            print("-------------")
    else:
        print("THIS IS NOT A VALID PLAY. CHECK FOR TYPOS")
    player=False
    computer=play_options[randint(0,2)]
