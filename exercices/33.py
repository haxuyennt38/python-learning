##Afficher les communs diverseurs du nombre naturel N

n = int(input())

for a in range (1, n + 1) :
    if n % a == 0 :
        print(a)
    else :
        print(' ')