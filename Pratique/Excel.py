file = open('list_de_note.csv', mode = "r", encoding = "utf-8-sig")

file_new = open('list_de_note_new.csv', mode = "w", encoding = "utf-8-sig")

header = file.readline() ##lire la premiere ligne

#file_new.write(header)

file_new.write(header.strip() + ", Điểm trung bình,Học lực\n")

row = file.readline() ##lire la deuxieme ligne
while row != "" :
    row_list = row.split(",")

    math = float(row_list[2])
    litt = float(row_list[3])

    ave = (math + litt)/2
    ave = round(ave,1)

    rank = ""
    
    if ave >= 8 :
            rank = "Giỏi"
    elif ave < 8 and ave >= 6.5 :
            rank = "Tiên tiến"
    else :
            rank = "Trung bình"

    row_new = row.strip() + "," + str(ave) + "," + rank + "\n"
    print(row_new)
    file_new.write(row_new)
    row = file.readline()

    
