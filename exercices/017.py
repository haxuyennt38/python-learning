print ('Salut, bienvenue dans ma super pyramide! Combien détage veux-tu?')
number = int(input())
for i in range (number):
    if i%2 !=0:
        print(i*'#', end= ' ')
    else :
        print('')