l = [1, 2, 3, 4, 4, 5, 67, 89, 10, 15, 19, 90]

a=filter(lambda a: a%5==0,l)


print(list(a))