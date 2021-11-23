##Calculer et afficher le nombre de Fibonacci

#Importer le nombre de n qui est le nombre naturel

n = int(input())

def fibonacci(n):
    f0 = 0;
    f1 = 1;
    fn = 1;
 
    if n < 0 :
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        for i in range(2, n):
            f0 = f1;
            f1 = fn;
            fn = f0 + f1;
        return fn;
number = "";
for i in range(1, n + 1):
    number = number + str(fibonacci(i)) + ", ";
print('The number is egal to :', number)