def tinhDiem(mon1, mon2, mon3):
    diemTB = (mon1 + mon2 + mon3) / 3
    return diemTB

def NhapDiemTuBanPhim():
    diemBaMon = []
    for item in range(3):
        while True:
            i = float(input("Nhap diem mon thu " + str(item + 1) + ": "))
            if 0 <= i <= 10:
                diemBaMon.append(i)
                break
            else:
                print("moi ban nhap lai")
    return print('Diem trung binh la: ', tinhDiem(diemBaMon[0],diemBaMon[1],diemBaMon[2]))
NhapDiemTuBanPhim()