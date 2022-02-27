def square(num):
    return num*num

l=[1,2,3]

apk=[]

for item in l:
    apk.append(square(item))

print(apk)    

print(list(map(square, l)))