list = [1,2,3,4,5,6]

for index,i in list:
    if i < 4:
        print('hello')
        list[index] = 0

print(list)
