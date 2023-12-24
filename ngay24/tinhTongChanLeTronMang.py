def nhapMang():
    doDaiMang = int(input('Nhap do dai cua mang: '))
    mangSo = []
    for i in range(doDaiMang):
        phantu = input("Nhap so thu " + str(i + 1) + ": ")
        mangSo.append(int(phantu))
        return mangSo

def nhapMangXetKieuBien():
    doDaiMang = int(input('Nhap do dai cua mang: '))
    mangSo = []
    for i in range(doDaiMang):
        while True:
            try:
                phantu = int(input("Nhap so thu " + str(i + 1) + ": "))
                mangSo.append(phantu)
                break
            except ValueError:
                print("Xin moi nhap lai!")
                continue
    return mangSo

def tinhTongChanVaLe(danhsach):
    tongChan = 0
    tongLe = 0
    for i in range(len(danhsach)):
        if danhsach[i] % 2 == 0:
            tongChan += danhsach[i]
        if danhsach[i] % 2 == 1:
            tongLe += danhsach[i]
    return [tongChan,tongLe]

mangSoDuocNhap = nhapMang()

print(tinhTongChanVaLe(mangSoDuocNhap))