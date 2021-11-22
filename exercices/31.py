##Calculer le produit du total nombre pair et du total nombre impair par le nombre naturel N

n = int(input())

if n < 0 :
    print('ne pas calculer ce produit')
else :
    nombrepair = 0
    nombreimpair = 0
    for i in range (1, n + 1) :
        if i % 2 == 0 :
            nombrepair = nombrepair + i
            i += 1
        elif i % 2 != 0 :
            nombreimpair = nombreimpair + i
produit = nombrepair * nombreimpair
print('Ce produit est :', produit)


