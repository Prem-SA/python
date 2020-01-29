import random
hidden = random.randint(1, 100)
print("you have 3 chances")
n=3
for i in range(3):
    guess = int(input("Please enter your guess: "))
     
    if guess == hidden:
        print ("Hit!")
    elif guess < hidden:
        print ("too low")
    else:
        print ("too high")
