a = input(int()) #la premiere longueur 

b = input(int()) #la deuxieme longueur

c = input(int()) #la troisieme longueur

if a + b > c and a + c > b and b + c > a :
    print('it is the triangle')
else :
    print('it is not the triagle')