from django.contrib import admin
from .models import TaiKhoan, AdminAccount, Employee, Customer, LichDatSan, Hoadon, Guest
# Register your models here.
models = [AdminAccount, Employee, Customer, LichDatSan, Hoadon, Guest]
admin.site.register(models)

