#Giải Phương Trình Bậc 2
import math
#Khai báo biến a b c dạng interger
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
#denta
d=(math.pow(b,2)) - 4 *a*c
if d ==0:
    e=(-b)/(2*a)
    print("Phương Trình Có nghiệm kép x1=x2=",e)
elif d<0:
    print("Phương Trình Vô Nghiệm")
elif d>0:
    x1=(-b+(math.sqrt(d)))/2*a
    x2=(-b-(math.sqrt(d)))/2*a
    print("Phương Trình Có 2 nghiệm phân biêt: \n","\t x1=",x1,"và x2=",x2)
else:
    print("Bạn vừa nhập không phải phương trình bậc 2 ")