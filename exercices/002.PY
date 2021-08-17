def getInfo(greeting, name) :
    return greeting + name + str('!')
name = str(input())
greeting = 'Salut,'
info = getInfo(greeting, name)
print(info)