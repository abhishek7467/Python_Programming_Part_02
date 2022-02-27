a=[3,2,4,2,5,7,9,7,5,5]

'''b=[]
for item in a:
    if item%2==0:
        b.append(item)


print(b) '''
#shortcut to write same...
b= [i for i in a if i%2==0]
print(b)



