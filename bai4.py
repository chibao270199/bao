#tạo một lớp hình vuông
class Hinh_vuong:
    #khai báo biến chiều dài và rôngj
    def __init__(self,chieu_dai,chieu_rong):
        self.dai = chieu_dai
        self.rong = chieu_rong
    #tính chu vi hình vuông
    def chu_vi(seft):
        return (seft.dai+seft.rong)*2
    def dien_tich(seft):
        return seft.rong*seft.dai
a=(int(input("Hãy Nhập Chiều Dài: ")))
b=(int(input("Hãy Nhập Chiều Rộng: ")))
c=Hinh_vuong(a,b)
print("Chu Vi Hình Chử Nhật là: ",c.chu_vi())
print("Diện Tịch Hình Chử Nhật là: ",c.dien_tich())