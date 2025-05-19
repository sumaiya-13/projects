"""
import random
computer=random.choice([1,2,3])
you=input("enter your choice: ").lower()
dic={"rock":1,"paper":2,"scissor":3}
you_choice=dic[you]
if you not in dic:
   print("invalid input!please,choode from\nrock\npaper\nscissor")


dic_com={1:"rock",2:"paper",3:"scissor"}
com_choice=dic_com[computer]
print("you entered:",you)
print("computer entered:",com_choice)

if computer==1 and you=="paper":
  print("you won!")
elif computer==2 and you=="scissor":
  print("you won!") 
elif computer==3 and you=="rock":
  print("you won!")
elif computer==2 and you=="rock":
  print("computer won!")
elif computer==3 and you=="paper":
  print("computer won!")
elif computer==1 and you=="scissor":
  print("computer won!")
else:
  print("draw")      

"""









import random

dic = {"rock": 1, "paper": 2, "scissor": 3}
dic_com = {1: "rock", 2: "paper", 3: "scissor"}

you = input("Enter your choice (rock, paper, scissor): ").lower()

if you not in dic:
    print("Invalid choice!")
else:
    computer = random.choice([1, 2, 3])
    you_choice = dic[you]
    com_choice = dic_com[computer]

    print("You entered:", you)
    print("Computer entered:", com_choice)

    if you_choice == computer:
        print("Draw!")
    elif (you_choice == 1 and computer == 3) or \
         (you_choice == 2 and computer == 1) or \
         (you_choice == 3 and computer == 2):
        print("You won!")
    else:
        print("Computer won!")






"""just a simple rock paper scissor game 
   if it is help full so yeahh keep watching my repo'ssssssssss........
   """
