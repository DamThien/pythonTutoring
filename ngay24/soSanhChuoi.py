
def nhapVaSoSanhChuoi():
    chuois = []
    for i in range(2):
        a = input('nhap chuoi ' + str(i + 1) + ': ')
        chuois.append(a)
    if soSanhChuoi(chuois[0],chuois[1]) == 1:
        return "Do dai chuoi 1 dai hon chuoi 2"
    elif soSanhChuoi(chuois[0],chuois[1]) == 2:
        return "Do dai chuoi 2 dai hon chuoi 1"
    elif soSanhChuoi(chuois[0],chuois[1]) == 0:
        return "2 chuoi dai bang nhau"
    
def soSanhChuoi(chuoi1, chuoi2):
    dai1 = len(chuoi1)
    dai2 = len(chuoi2)
    if dai1 == dai2:
        return 0
    elif dai1 > dai2:
        return 1
    else:
        return 2
    
print(nhapVaSoSanhChuoi())