import math
import fractions #thu vien xuat nghiem kep

try:
    with open('phuongtrinhdauvao.txt', mode='r') as Phuong_trinh_dau_vao:
        readline_1 = Phuong_trinh_dau_vao.readline().strip('\n\n')
        
        #NẾU CHỌN GIẢI PHƯƠNG TRÌNH BẬC 1:
        if readline_1 == '1':
            readline_2 = Phuong_trinh_dau_vao.readline().strip('\n')
            a,b = map(float,readline_2.split())
            if a == 0 and b == 0:
                notice = "Phương trình có vô số nghiệm"
            elif a == 0 and b != 0:
                notice = "Phương trình vô nghiệm"
            else:
                PT_1nghiem = -b/a
                notice = ("Phương trình có 1 nghiệm duy nhất là\n X = {} ".format(PT_1nghiem))
        
        #NẾU CHỌN GIẢI PHƯƠNG TRÌNH BẬC 2
        elif readline_1 == '2':
            readline_2 = Phuong_trinh_dau_vao.readline().strip('\n')
            a,b,c = map(float,readline_2.split())
            
            #TÍNH DELTA
            nghiem_kep =fractions.Fraction(-b / (2*a))
            delta = b*b - 4*a*c
            
            if delta > 0:
                X_1 = (-b + math.sqrt(delta))/(2*a)
                X_2 = (-b - math.sqrt(delta))/(2*a)
                notice = ("Phương trình có 2 nghiệm phân biệt:\n X1 = {}\n X2 = {}".format(X_1,X_2))
            
            elif delta == 0:
                notice = ("Phương trình có nghiệm kép là X1 = X2 = {} ".format(nghiem_kep))

            elif delta < 0:
                notice =("Phương trình đã cho vô nghiệm")

        #NẾU CHỌN SAI Ở DÒNG 1
        elif readline_1 != '1' or '2':
            notice =("Vui lòng chọn lại định dạng 1 hoặc 2 ở dòng thứ nhất")

except FileNotFoundError:
    notice =("File not found")


except:
    notice = ("Bạn đã nhập sai định dạng")

with open("output.txt", mode='wb')  as file_output:
    file_output.write(notice.encode('utf8'))
    

