from django.db import models

# Create your models here.
class TaiKhoan(models.model):
    hoten = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    matkhau = models.CharField(max_length=255)
    vaitro = models.CharField(
        max_length=10,
        choices=[("Admin", "Admin"), ("Employee", "Employee"), ("Customer", "Customer")],
        default="Customer"
    )

    def capnhat_thongtin(seft, hoten=None, phone=None, email=None):
        if hoten:
            self.hoten = hoten
        if phone:
            self.phone = phone
        if email:
            self.email = email
        self.save()
        return f"Thông tin tài khoản {self.username} đã được cập nhật."
    def __str__(self):
        return self.username 
    
    class Admin(TaiKhoan):
        def quan_ly_he_thong(self):
            return f"Admin {self.username} đang quản lý hệ thống."
        def quan_ly_nhan_vien(self):
            return f"Admin {self.username} đang quản lý nhân viên."
        
    class Employee(TaiKhoan):
        def quan_ly_tai_khoan_khach_hang(self):
            return f"Nhân viên {self.username} đang quản lý tài khoản khách hàng."
        def lam_viec_phan_cong(self):
            return f"Nhân viên {self.username} đang thực hiện công việc được phân công."
        
    class Customer(TaiKhoan):
        makhachhang = models.CharField(max_length=20, unique=True)

        def dat_san(self, lich_dat_san):
            return f"Khách hàng {self.username} đã đặt sân {lich_dat_san.madon} vào ngày {lich_dat_san.batdau}."
        def huy_san(self, lich_dat_san):
            return f"Khách hàng {self.username} đã hủy sân {lich_dat_san.madon}."
        def danh_gia(self, san, rating, comment):
            return f"Khách hàng {self.username} đã đánh giá sân {san} {rating} sao với nhận xét: {comment}."
        
    class LichDatSan(models.Model):
        batdau = models.DateTimeField()
        ketthuc = models.DateTimeField()
        loaisan = models.CharField(max_length=50)
        thongtin_khachhang = models.ForeignKey(Customer, on_delete=models.CASCADE)
        madon = models.CharField(max_length=20, unique=True)

        def trang_thai_don_hang(self):
            return f"Lịch đặt sân {self.madon} đang được xử lý."
        def __str__(self):
            return f"Lịch {self.madon} từ {self.batdau} đến {self.ketthuc}"
        
    class Hoadon(models.Model):
        mahoadon = models.CharField(max_length=20, unique=True)
        thongtin_donhang = models.ForeignKey(LichDatSan, on_delete=models.CASCADE)
        thanhtoan_thanhcong = models.BooleanField(default=False)

        def thanh_toan(self):
            self.thanhtoan_thanhcong = True
            self.save()
            return f"Hóa đơn {self.mahoadon} đã được thanh toán thành công."
        def xuat_hoa_don(self):
            return f"Hóa đơn {self.mahoadon} với thông tin: {self.thongtin_donhang}."
        def __str__(self):
            return f"Hóa đơn {self.mahoadon}"
        
    class Guest(models.Model):
        def xem_thong_tin_san(self):
            return "Khách vãng lai đang xem thông tin sân."
        def tim_san(self, loaisan):
             return f"Khách vãng lai đang tìm sân loại {loaisan}."
        def tao_tai_khoan(self, email, hoten, matkhau, phone, username):
            customer = Customer.objects.create(
            email=email, hoten=hoten, username=username, matkhau=matkhau, phone=phone, makhachhang="KH001"
        )
            return customer
    