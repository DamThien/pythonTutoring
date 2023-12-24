# bai 1 ---------------

dem = '' #Khoi tao bien dem
for i in range(4): #Tao vong lap
    bien = input("nhap bien: ") #Khoi tao bien nhap vao tu man hinh
    doDaiBien = str(len(bien)) #Dem do dai cua bien
    dem = dem + doDaiBien + "-" #Gan bien Dem se bang voi no cong them chuoi nhap vao
ketqua = dem[:-1] #Cat chuoi cua bien dem de loai bo ki tu "-"
print(ketqua)

#  bai 2 ---------------

text = input('Nhap text: ')
count = 0 #Khoi tao bien dem "count"
doDai = len(text)
for i in range(doDai):
    if text[i] == "X": #Neu gia tri cua chi muc [i] bang X thi 'count' se them 1 don vi
        count =+ 1 # 'count' thay doi nen in good luon
        print("Good")
        break # khi gia tri cua chi muc [i] bang X thi dung vong lap For
if count == 0: # Neu 'count' khong thay doi thi in ra "Bad"
    print('Bad')

bien = 34

def chaoEm(a1: int, a2) -> str:
    print(isinstance(a1, int))
    print(isinstance(a2, int))
    print(a1*a2)

chaoEm("asdkjfhkaj",4)