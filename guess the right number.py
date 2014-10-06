#Jess Howard
#6/9/14
#class exercises
#Guess my number

print("Guess the number i am wanting!")
guess= int(input("please enter a number:"))
if guess<6:
    print("Sorry your number is to low try a number that is a bit higher.")
if guess>6:
    print("Sorry your number is to high try a number that is a bit lower.")
if guess == 6:
    print("You have guessed correctly the number is 6!")

