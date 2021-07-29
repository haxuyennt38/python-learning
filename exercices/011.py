#Virer les années
ageOfuser = int(input())
yeartoday = int(input())
count = 0
yearOfbirthday = yeartoday - ageOfuser
for year in range(yearOfbirthday, 2022) :
    print(f'Il y a {yeartoday - year} ans, tu avais {count} ans')
    count += 1
    