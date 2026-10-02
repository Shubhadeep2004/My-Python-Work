#Python numbe gussing game
import random
lowest_num=1
highest_num=100

answer=random.randint(lowest_num,highest_num)
guesses=0
is_running =True

print("Enter Your guess")
print(f"Enter a guess between {lowest_num} and {highest_num}")
while  is_running:
    guess=input("My guess is:")

    if guess.isdigit():
        guess=int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("The number is out of range")
            print(f"Enter a guess between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too Low!! try again")
        elif guess > answer: 
            print("Too high!! try again")
        else:
            print(f"The corect answer is {answer}") 
            print(f"The number of gusses it take is {guesses}")      
    else:
        print("INVALID INPUT")
        print(f"Enter a guess between {lowest_num} and {highest_num}")       