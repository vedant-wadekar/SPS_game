# stone(s) paper(p) siccor(r) game
import random
computer = random.choice([0,1,2])
youDict = { "s" : 1, "p" : 2, "r" :0 }
revDict = { 1 : "Stone" , 2 : "Paper", 0 : "Siccor"}
print(f"Computer choose {revDict[computer]}")
youstr = input("Enter the  word for [stone(s) paper(p) siccor(r)] : ")

you = youDict[youstr]
print(f"Computer choosed {revDict[computer]} and you choose {revDict[you]}")

if(computer == you):
     print("The match is draw !")
else:
    if(computer == 0 and you ==1):
        print("You win")
    elif(computer == 0 and you ==2):
        print("You lose")
    elif(computer == 1 and you ==2):
        print("You win")
    elif(computer == 1 and you ==0):
        print("You lose")
    elif(computer == 2 and you ==0):
        print("You win")
    elif(computer == 2 and you ==1):
        print("You lose")
    else:
        print("Something went wrong")
    