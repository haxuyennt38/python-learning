def getInf(name, birthday) :
    return name + ' ' + str(birthday)
name = "Haxuyen"
birthday = 38
info = getInf(name, birthday)
print(info)


def ton_age(age) :
    if ton_age >= 60 :
        return('agé')
    else:
        return('jeune')

age = input()
inFo = ton_age(age)
print(inFo)