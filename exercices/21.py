##Type de triangle

#first number : a>0
a = int(input())

#second number : b>0
b = int(input())

#third number : c>0
c = int(input())

if a == c and b == c :
    print('it is the equilateral triangle')
elif a == b or b == c or a == c :
    print('it is the isosceles triangle')
elif c * c == b * b + a * a or a * a == b * b + c * c or b * b == c * c + a * a :
    print('it is the right triangle')
elif c * c == b * b + a * a and b == a or a * a == b * b + c * c and b == c or b * b == c * c + a * a and c == a :
    print('isosceles and right')
else :
    print('it is the triangle')

