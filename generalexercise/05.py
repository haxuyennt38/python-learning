##Write a program to input from the input file a familiar greeting of any length, each word on a line. Output the greeting file you just received on a single line, the words separated by a space
#Mo file voi mode='r' de doc file
with open('05_ip.txt', 'r') as fileInp:

#Dung ham read() doc toan bo du lieu tu file
    Filecomplete = fileInp.read()

#Dung ham splitlines() cat du lieu theo tung dong va luu thanh danh sach
listOfligne = Filecomplete.splitlines()

#Dung ham join() noi cac dong du lieu lai cach nhau 1 khoang trang
phrasecomplete = ' '.join(listOfligne)
print(phrasecomplete)

#Mo file voi mode='w' de ghi file
with open('05_out.txt', 'w') as fileOut:

   #Ghi noi dung vao file
   fileOut.write(phrasecomplete)
