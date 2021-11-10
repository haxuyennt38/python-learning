a = int(input()) #la premiere longueur 

b = int(input()) #la deuxieme longueur

c = int(input()) #la troisieme longueur

if a + b > c and a + c > b and b + c > a :
    print('it is the triangle')
else :
    print('it is not the triagle')