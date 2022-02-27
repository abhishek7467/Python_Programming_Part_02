try:
    a= int(input("Enter a Number"))
    c=1/a
    print(c)

except ValueError as e:
        print("Please Enter a Valid Value::")

except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0")


print("Thanks for using this code!")
