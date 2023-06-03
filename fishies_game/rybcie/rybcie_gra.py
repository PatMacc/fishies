# I'll start from introducing player (you) to opponent (computer)

print("Welcome in the Aquarium! \nNow you are doomed to play with me!... at least for once please. \nI've been so lonely lately...")
name = input("How can I call You? (insert name): ")

# Developing main game mechanics, which ofc. are going to be named "game". Whole concept is based on rock, paper, scissors game
# with some extensions for the sake of game dynamics and making this project more enjoyable than flatlined "what is stronger".

def game():
    print("Choose your fishy, " +  name + "\n(1) Small, \n(2) Medium, \n(3) Biggie")
    fish_type = input()
    

    import re
    
    if re.search ("^(S|s).*[mMaAlL]l|L$", fish_type):
        fish_type = 1
        game2(fish_type)
    elif re.search ("^(M|m).*[eEdDiIuUmM]m|M$", fish_type):
        fish_type = 2
        game2(fish_type)
    elif re.search ("^(B|b).*[iIgGeE]e|E$", fish_type):
        fish_type = 3
        game2(fish_type)
    else:
        print("Ummm? Choose again")
        game()

your_wins = 0
draws = 0
my_wins = 0
        
def game2(x):
    import random
    choices = ["Small", "Medium", "Biggie"]
    computer = random.choice(choices)
    print("I choose" , computer)

    if computer == "Small":
        computer = int(1)
    if computer == "Medium":
        computer = int(2)
    if computer == "Biggie":
        computer = int(3)

    #your_wins = 0
    #draws = 0
    #my_wins = 0
    if x < computer:
        print ("I won, looser!")
        global my_wins
        my_wins += 1

    if x == computer: 
        print ("Well, that's uncomfortable...")
        global draws
        draws += 1
    if x > computer:
        print("This can't be!!!")
        global your_wins
        your_wins += 1
    game3(my_wins,draws,your_wins)





def game3(i,j,k):
    print("Shall we continue?\nType '+' to continue or '-' to end our little game")
    decision = input()
    if decision == "+":
        decision = True
        print("Okay, let's go!")
        game()

    elif decision == "-":
        decision = False
        print("Until we meet again!\nHere is the score:")
        print ("I won" , i , "times")
        print ("You won", k , "times")
        print("Our draws:" , j)

        print ("Have a nice day!\n\n\nPlease consider hiring me :)")



    
game()


    





    
    

 





