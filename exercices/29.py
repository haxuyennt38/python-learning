## Calculate S(n) = 1 - x + x^2/2! - x^3/3! + … - x^(2n-1)/(2n-1)! + x^(2n)/(2n)!

# importer le factoriel de n

n = int(input())
x = float(input())

# Calculer le S(n) 
result = 1
factorial = 1
if n < 0 :
    print('I do not calculate the S')
elif n == 0 :
    print('S(n) = 1')
else :
    for i in range(1, 2 * n + 1) : ##i la chi so mu
        if i % 2 == 0 :
            factorial += i 
            result += pow(x, i)/factorial #x**i ou x^i
        else :
            result -= pow(x, i)/factorial
    print('{:.5f}'.format(result))


