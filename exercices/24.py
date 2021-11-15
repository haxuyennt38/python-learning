##Use the circle 'for'

# input a and b
a = int(input())
b = int(input())

total = 0
if a > b :
    print('it is not the total')
else :
    for index in range(a, b+1) :
        total += 1
    print('it is the total : ', total)