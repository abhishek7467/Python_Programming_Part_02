#This concept is used for the prevent error in programm.

while(True):
    print("Press q to quit")
    a = input("Enter The Number:")

    if a=='q':
        break
    try:
        a=int(a)
        if a>6:
            print("You Entered a greater number then 6")
    except Exception as e:
        print(f"Your input resulted in an error {e}")    

print("Thanks for playing this game!")