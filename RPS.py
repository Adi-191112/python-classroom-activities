import random
while True:
    user_input = input("Enter the choice-rock, paper, scissors")
    possible_input = ["rock","paper","scissors"]
    computers_input = random.choice(possible_input)
    print(f"your choice is {user_input} computers choice is {computers_input}")
    if user_input == computers_input:
        print("it is a tie") 

    elif (user_input == "rock"):
        if(computers_input == "paper"):
            print("you lose, better luck next time")
        else:
            print("you win")
    elif(user_input == "paper"):
        if(computers_input == "rock"):
            print("you win")
            
        else:
            print("you lose, better luck next time")

    elif(user_input == "scissors"):
        if(computers_input == "rock"):
            print("you win")
            
        else:
            print("you lose, better luck next time")
            

            

        
    

    
