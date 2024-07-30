import random
print("Welcome to the game of Rock, Paper and Scissors")

play = ["Rock", "Paper", "Scissors"]
computer = play[random.randint(0,2)]

#Set the player to False
Running = False
p=0
c=0
t=1

while Running == False:
#Set the player to True

    player = input("Rock, Paper, Scissors? ").lower()
    print("Computer chose:",computer)
    print("player chose:",player)
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            c+=1
        else:
            print("You win!", player, "smashes", computer)
            p+=1
    elif player == "paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
            c+=1
        else:
            print("You win!", player, "covers", computer)
            p+=1
    elif player == "scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            c+=1
        else:
            print("You win!", player, "cuts", computer)
            p+=1
    else:
        print("That's not a valid play. Check the spelling!")
    x= input("Wanna play again? (y/n) ")


    if x== "n":
      Running = True
      print("\n\nFinal score after",t,"rounds is:","\n Player:",p,"\n Computer:",c)
    else:
      Running= False
      computer = play[random.randint(0,2)]
      t+=1
    #Player was set to True, but we want it to be False so the loop continues
