#kiểm tra Số nguyên tố
a = int(input("Mời bạn nhập số: "))
if (a > 1 and a % 2 != 0 and a%7 != 0 and a!=9):
    print(a,"Là số nguyên tố ")
else:
    print(a,"Không phải là số nguyên tố")