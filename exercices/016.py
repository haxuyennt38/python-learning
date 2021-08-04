#Nombre entre 1 et 25
print('Salut, bienvenue dans ma super pyramide! Combien détages veux-tu?')
def pypart2 (number):
    #number of spaces
    k = 2*number - 2
    for i in range(0, number): #row
        for j in range(0, k) :
            print(end= ' ')
        #Decrementing k after each loop
        k = k - 2
        for j in range(0, i+1): #colonne
            print('# ', end='')
        print('\r')

number = int(input())
pypart2 (number)
        