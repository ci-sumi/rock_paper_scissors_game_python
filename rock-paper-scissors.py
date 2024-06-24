import random

user_wins=0
computer_wins=0
options=['rock','paper','scissors']
while True:
    user_input=input("Enter user choices Rock/Paper/Scissors/Q:?").lower()
    if(user_input=="q"):
            break
    if  user_input not in options:
         continue
    
    random_number=random.randint(0,2)
    comupeter_pick=options[random_number]
    if(user_input=='rock' and comupeter_pick=='scissors'):
        print("you win")
        user_wins+=1
        
    elif(user_input=='scissors' and comupeter_pick=='paper'):
        print("you win")
        user_wins+=1
        
        
    elif(user_input=='paper' and comupeter_pick=='rock'):
        print("you win")
        user_wins+=1
        
    
    else:
        print("computer wins")
        computer_wins+=1
     
  
  
     
print(f"you won {user_wins} times")
print(f"computer wins{computer_wins} times")
        