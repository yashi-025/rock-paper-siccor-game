# rock-paper-siccor-game
import random
def game():
    option="rps"
    char=random.choice(option)
    guess=None
    while True:
        guess=input("enter the 1st letter of your choice out of rock,paper,siccsor:")
        print("user's choice: ",guess)
 
        print("computer's choice: ",char)
        if guess==char:
            print("tie as both choice are same") 
        elif guess=="r" and char=="p" or guess=="s" and char=="r" or guess=="p" and char=="s":
            print("you lost!")
        elif guess=="r" and char=="s" or guess=="s" and char=="p" or guess=="p" and char=="r" :
            print("you won :)") 
        enter=input("you want to play next y/n:").lower()
        if enter!="y":
            print("nice to play with you :)")  
            break         
game()               
