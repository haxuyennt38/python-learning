##Hien thi cac so chia het cho 5 trong khoang a, b (a<=b)

a = int(input())
b = int(input())


if a > b :
    print('First number is bigger than second number')
else :
    compte = 0
    for i in range (a, b + 1) :
          if i % 5 == 0:
               #Dem cac so thoa dieu kien
               compte += 1
               #Kiem tra vuot qua 10 so hay chua
               if compte > 10:
                   print("\nIn qua 10 so roi!")
                   #Thoat vong lap
                   #break
               print(i, end=" ")
       #Neu khong gap lenh break thi se thuc hien lenh else
    else:
           if compte == 0:
               print("Khong co so nao chia het cho 5")
           else:
               print("\nDa in het cac so chia het cho 5")




