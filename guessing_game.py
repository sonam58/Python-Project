import random

number_of_guesses = 0
print("Number of guesses is limited to only 10 times")
print("Guess the number from 1 to 20")
comp_number = random.randint(1,20)

while number_of_guesses <= 10:
    print("Guess the number:")
    user_number = int(input())
    
    if user_number < comp_number:
        print("oh No!you guessed the lesser number")
        
    elif user_number > comp_number:
         print("Oops!You guessed the greater number")
        
    else:
        print("The random number: ",comp_number)
        print("congrates!You guess the right number")
        print("you tried ",number_of_guesses+1 ,"times.")
        print(10-number_of_guesses-1, "chances are left")
        break
    
    print(10-number_of_guesses-1, "chances are left")
    number_of_guesses = number_of_guesses+1

    
    if (number_of_guesses == 10):
        print("finished! do better next time")
        break
        
    


    

        
   
    
        
    
