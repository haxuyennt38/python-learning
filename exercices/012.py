ageOfuser = int(input())
yeartoday = int(input())
yearOfbirthday = yeartoday - ageOfuser
count = 0
for year in range (yearOfbirthday, 2022) :
    haftage = (yeartoday - year) / 2
    if haftage > 0 :
        print(f'Il y a {yeartoday - year} ans, tu avais la moitié de lâge que tu as aujourdhui')
    else :
        print(f'Il y a {yeartoday - year}, tu avais {count} ans')
    count += 1