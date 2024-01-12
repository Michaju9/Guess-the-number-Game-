from random import randint

los = randint(1,10)
odp = -1
i = 0
print("Guess the number from the range 1 - 10")

while odp != los:
    i += 1
    odp = int(input("Enter a number: "))
    if odp > los:
        print("Unfurtunately, the randomly chosen number is smaller than yours")
    elif odp < los:
        print("Unfortunately, the randomly chosen number is greater than yours")
print("Congratulations! You guessed it in", i, "attempts.")