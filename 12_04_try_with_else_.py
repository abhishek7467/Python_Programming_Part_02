try:
    i=int(input("Enter a Number!"))
    c=1/i
except Exception as e:
    print(e)
else:
    print("we were successful!")    