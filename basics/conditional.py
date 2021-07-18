note = int(input("Nhat so diem cua ban :"))
#if note < 10 :
#     print('Echec')
# else :
#     print('pass')
# print('Echec') if note < 10 else print('pass')
result = ''  
if note < 10 :
    result = "Echec"
elif 10 <= note <= 12 :
    result = "Valide"
elif 12 <= note <= 15 :
    result = "Bien"
elif 15 <= note <= 18 :
    result = "Tresbien"
else :
    result = "Excelent"
print(result)
