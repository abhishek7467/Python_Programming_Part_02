def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is not good _ abhishek")

a= increment(99)
print(a)
