import random
randNumber = random.randint(1,5)
print(randNumber)
userGuess=None
guesses=0



while userGuess!=randNumber:
    userGuess= int(input("Enter your guess:"))
    if userGuess==randNumber:
        print("You gessed it right!")
    else:
        if userGuess>randNumber:
            print("You gessed it wrong! Enter a smaller number")
        else:    
            print("you gessed it wrong! Enter a Greater Number")    
    guesses+=1

print(f"You gessed the number in {guesses} gesses")


with open("hoiscore.txt","r") as f:
    hiscore=int(f.read())

if guesses<hiscore:
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))