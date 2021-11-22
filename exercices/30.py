##afficher un numéro qui renverse à un numéro naturel

#importer du numéro par le clavier

n = int(input())

#Vérifier ce numéro qui assure plus de zéro ou pas

if n < 0 :
    print('Ne pas déterminer ce numéro')
else :
    numerorenverse = 0
    while n > 0 :
        numerofinal = n % 10
        numerorenverse = numerorenverse * 10 + numerofinal
        n = n // 10
    print(numerorenverse)
