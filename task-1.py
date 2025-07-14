import random
choices = ["rock", "paper", "scissors"]
user_score=0
computer_score=0
print("welcome to rock, paper and scissor")
user=input("Enter rock, paper and scissors: ").lower()
computer = random.choice(choices)

print(f"Computer chose: {computer}")

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
    user_score+=1
else:
    print("You lose!")
    user_score+=1
    
print("final_score:")
print("your_score",user_score)
print("computer_score", computer_score)
if user_score==computer_score:
    print("The game is tie!")
elif user_score>computer_score:
    print("You won the game")
else:
    print("computer won the game")

play_again=input("Play_again(yes or no):")  
if play_again =="yes":
    print("Thank you for playing")
elif play_again =="no":
    print("Thankyou") 
    feedback=input("Enter the your feedback:")
    print("Thank you for your feedback")
else:
    print("invalid")  