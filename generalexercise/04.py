##it is necessary to calculate a list of the random relative integer

#show a list
integerrelative = input()


#show each number in the list thanks to the way the code is used: split ()
eachnumberOfalist = integerrelative.split()

#the number you need to find
number = map(int, eachnumberOfalist)

#calculate the total
total = sum (number)

print (total)



