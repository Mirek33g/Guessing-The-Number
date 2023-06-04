from art import logo 
import random 

print(logo) 
print()
print("Welcome to the Number Guessing Game!")
print("I'm thinking of the number between 1 and 100.")
difficulty = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()


random_number = random.randrange(1,101) 
user_guess = 0

#def printing():
 # print("---------")
#  print(f"You have {lvl} attempts left. Try again")


def checking(lvl):
  while lvl >= 0:
    user_guess = int(input("Make a guess: ")) 
    lvl -= 1
    
    if lvl == 0:
      print(f"You have {lvl} attempts left. Sorry you lost the game.")
      
    elif user_guess == random_number:
      print("---------")
      print(f"Congratulations you have guessed with {lvl} attempts left")
      lvl = 0
      
    elif user_guess > random_number: 
      print("------------")
      print(f"You have {lvl} attempts left. Try again")
      print("Your number is too high")
      
    elif user_guess < random_number:
      print("---------")
      print(f"You have {lvl} attempts remaining to guess the number.")
      print("Your number is too low")
    elif lvl == 0:
      print(f"You have {lvl} attempts left. You lost the game.")


if difficulty  == "hard":
  print("You have 5 attempts to guess the number.") 
  checking(5)
  
elif difficulty == "easy":
  print("You have 10 attempts to guess the number")
  checking(10) 

#commit
  