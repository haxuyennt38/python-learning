def listing(dict) :
    liste = []
    for i in dict :
        if dict[i] > 10 :
            liste.append(i)
    return liste


notes = {'Lina' : 8, "Linda" : 11, 'Tom' : 6, 'Julien' : 12}

print(listing(notes))