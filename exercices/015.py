#Nombre entre 1 et 25
print('Salut, bienvenue dans ma super pyramide! Combien détages veux-tu?')
def pypart (number):
    for i in range(0, number): #row
        for j in range(0, i+1): #colonne
            print('#', end='')
        print('\r')

number = int(input())
pypart (number)
        