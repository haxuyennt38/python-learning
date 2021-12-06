def ton_age(age) :
    if age >= 60 :
        return ('agé')
    else:
        return ('jeune')

age = int(input())
inFo = ton_age(age)
print(inFo)