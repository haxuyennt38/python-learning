##Hien thi bang cua chuong n voi n tu 1 den 9
try :
    n = int(input())
    if n <1 or n >9 :
        print('Chi lay gia tri trong khoang tu 1 den 9')
    else :
        for i in range(1, 10) :
            print("{} x {} = {}".format(n, i, n * i))

except :
    print('Bang cuu chuong khong hop le')