a=56#global variable
def fucn1():
    global a
    print(f"Print statement 1: {a}")

    a=9#local variably
    print(f"Print Statement 2: {a}")
    

fucn1()
print(f"print statement 3: {a}")
