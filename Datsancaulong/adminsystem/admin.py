from django.contrib import admin
from .models import TaiKhoan, AdminAccount, Employee, Customer, LichDatSan, Hoadon, Guest

# Register your models here.

# models = [AdminAccount, Employee, Customer, LichDatSan, Hoadon, Guest]
# admin.site.register(models)



class AdminAccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'hoten', 'vaitro')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'hoten', 'vaitro')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'hoten', 'vaitro', 'makhachhang')

class LichDatSanAdmin(admin.ModelAdmin):
    list_display = ('madon', 'batdau', 'ketthuc', 'loaisan', 'thongtin_khachhang')

class HoadonAdmin(admin.ModelAdmin):
    list_display = ('mahoadon', 'thongtin_donhang', 'thanhtoan_thanhcong')

admin.site.register(AdminAccount, AdminAccountAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(LichDatSan, LichDatSanAdmin)
admin.site.register(Hoadon, HoadonAdmin)
admin.site.register(Guest)