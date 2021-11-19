## Calculer et afficher le factoriel

# taper directement le clavier

n = int(input())

# Calculer le factoriel

if n < 0 :
    print('no factorial exists')
elif n == 0 :
    print('the factorial is egal to 1')
else :
    factorial = 1
    for i in range (1, n + 1) :
        factorial *= i
print(factorial)


