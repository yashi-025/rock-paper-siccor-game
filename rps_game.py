rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_image=[rock, paper, scissors]
option=["rock", "paper", "scissors"]
while True:
    user_choice=input("choose rock,paper,scissors:\t")
    print(game_image[option.index(user_choice)])
    
    computer_choice=random.choice(option)
    print(f"computer's choice: {computer_choice}")
    print(game_image[option.index(computer_choice)])
    
    if user_choice=="rock" and computer_choice=="scissors":
        print("you win")
    elif user_choice=="paper" and computer_choice=="rock":
        print("you win")
    elif user_choice=="scissors" and computer_choice=="paper":
        print("you win")
    elif user_choice==computer_choice:
        print("draw")
    else:
        print("computer wins")
    more_turn = input("whether you want to play more: y/n? ")
    if more_turn!="y":
            print("nice to play with you :)")  
            break