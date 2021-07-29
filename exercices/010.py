#Display ages
yeartoday = int(input())
yearOfbirthday = int(input())
year = yearOfbirthday 
while year <= yeartoday :
    age = year - yearOfbirthday
    year += 1
    #print(f'{year} - {age} year olds')
    if age <=1 :
        print(f'{year} - {age} year old')
    else :
        print(f'{year} - {age} year olds')

    

