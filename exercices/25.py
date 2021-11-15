####Use the loop 'while'

# input a and b
a = int(input())
b = int(input())

if a > b :
    print('it is not the total')
else :
    i = a
    total = 0
    while i <= b :
        total += i
        i += 1 
    print(total)