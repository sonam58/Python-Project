import random

comp_wins = 0
player_wins = 0

def Choose_Option():
    user_choice = input("choose Rock,Paper or Scissor: ")
    if user_choice in ["Rock","rock","R","r"]:
        user_choice = "r"
    elif user_choice in ["Paper","paper","P","p"]:
        user_choice = "p"
    elif user_choice in ["Scissor","scissor","S","s"]:
        user_choice = "s"
    else:
        print("I dont't understand try again.")
        Choose_Option()
    return user_choice


def Computer_Option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
    print("")


    user_choice = Choose_Option()
    comp_choice = Computer_Option()


    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("You choose rock.The computer choose rock.You tied.")

        elif comp_choice == "p":
            print("You choose rock.The computer choose paper.You lose.")
            comp_wins += 1

        elif comp_choice == "s":
            print("You choose rock.The computer choose scissor.You win.")
            player_wins += 1


    elif user_choice == "p":
        if comp_choice == "r":
            print("You choose paper.The computer choose rock.You win.")
            player_wins += 1

        elif comp_choice == "p":
            print("You choose paper.The computer choose paper.You tied.")

        elif comp_choice == "s":
            print("You choose paper.The computer choose scissor.You lose.")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("You choose scissor.The computer choose rock.You lose.")
            comp_wins += 1

        elif comp_choice == "p":
            print("You choose scissor.The computer choose paper.You win.")
            player_wins += 1

        elif comp_choice == "s":
            print("You choose scissor.The computer choose scissor.You tied.")

    print("")
    print("player wins: "+str(player_wins))
    print("computer wins: "+str(comp_wins))
    print("")


    user_choice = input("Do you want to continue playing?(y/n)")
    if user_choice in ["Y","y","yes","Yes"]:
        pass
    elif user_choice in ["N","n","no","No"]:
        break
    else:
        break

    
            
        

        
            
