from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

############################# 管理者設定類別####################################


class Category(models.Model):
    Department = models.CharField(max_length=15)
    Category_A = models.IntegerField(default=0)
    Category_B = models.IntegerField(default=0)
    Category_C = models.IntegerField(default=0)
    Category_D = models.IntegerField(default=0)
    Category_E = models.IntegerField(default=0)

    Category_F = models.IntegerField(default=0)
    Category_G = models.IntegerField(default=0)
    Category_H = models.IntegerField(default=0)
    Category_I = models.IntegerField(default=0)
    Category_J = models.IntegerField(default=0)

    Category_K = models.IntegerField(default=0)
    Category_L = models.IntegerField(default=0)
    Category_M = models.IntegerField(default=0)
    Category_N = models.IntegerField(default=0)
    Category_O = models.IntegerField(default=0)

    Category_P = models.IntegerField(default=0)
    Category_Q = models.IntegerField(default=0)
    Category_R = models.IntegerField(default=0)
    Category_S = models.IntegerField(default=0)
    Category_T = models.IntegerField(default=0)

    Category_U = models.IntegerField(default=0)
    Category_V = models.IntegerField(default=0)
    Category_W = models.IntegerField(default=0)
    Category_X = models.IntegerField(default=0)
    Category_Y = models.IntegerField(default=0)

    Category_Z = models.IntegerField(default=0)

    # is_active = models.BooleanField(default=True)

class Subcategory(models.Model):
    Category = models.CharField(max_length=15)
    Subcategory_A = models.CharField(max_length=15, default="0")
    Subcategory_B = models.CharField(max_length=15, default="0")
    Subcategory_C = models.CharField(max_length=15, default="0")
    Subcategory_D = models.CharField(max_length=15, default="0")
    Subcategory_E = models.CharField(max_length=15, default="0")

    Subcategory_F = models.CharField(max_length=15, default="0")
    Subcategory_G = models.CharField(max_length=15, default="0")
    Subcategory_H = models.CharField(max_length=15, default="0")
    Subcategory_I = models.CharField(max_length=15, default="0")
    Subcategory_J = models.CharField(max_length=15, default="0")

    Subcategory_K = models.CharField(max_length=15, default="0")
    Subcategory_L = models.CharField(max_length=15, default="0")
    Subcategory_M = models.CharField(max_length=15, default="0")
    Subcategory_N = models.CharField(max_length=15, default="0")
    Subcategory_O = models.CharField(max_length=15, default="0")

    Subcategory_P = models.CharField(max_length=15, default="0")
    Subcategory_Q = models.CharField(max_length=15, default="0")
    Subcategory_R = models.CharField(max_length=15, default="0")
    Subcategory_S = models.CharField(max_length=15, default="0")
    Subcategory_T = models.CharField(max_length=15, default="0")

    Subcategory_U = models.CharField(max_length=15, default="0")
    Subcategory_V = models.CharField(max_length=15, default="0")
    Subcategory_W = models.CharField(max_length=15, default="0")
    Subcategory_X = models.CharField(max_length=15, default="0")
    Subcategory_Y = models.CharField(max_length=15, default="0")

    Subcategory_Z = models.CharField(max_length=15, default="0")


class Product(models.Model):
    Category = models.CharField(max_length=15)
    Subcategory_en = models.CharField(max_length=15)
    Subcategory = models.CharField(max_length=15)
    Number = models.CharField(max_length=20)
    Name = models.CharField(max_length=100)
    Specification = models.CharField(max_length=50)
    Unit = models.CharField(max_length=10)


class Department(models.Model):
    DeptName = models.CharField(max_length=200)

    def __str__(self):
        return self.DeptName

# 電機科table
# 改成各科資料表(由Department分類)


class MaterialStock(models.Model):
    Dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    Category = models.CharField(max_length=15)
    Subcategory_en = models.CharField(max_length=15)
    Subcategory = models.CharField(max_length=15)
    Number = models.CharField(max_length=20)
    Name = models.CharField(max_length=100)
    Specification = models.CharField(max_length=50)
    Unit = models.CharField(max_length=100)
    Quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.Category


class MaterialStocklog(models.Model):
    Dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    Category = models.CharField(max_length=15)
    Subcategory_en = models.CharField(max_length=15)
    Subcategory = models.CharField(max_length=15)
    Number = models.CharField(max_length=20)
    Name = models.CharField(max_length=100)
    Specification = models.CharField(max_length=50)
    Unit = models.CharField(max_length=100)
    Quantity = models.IntegerField(default=0)
    datetime = models.CharField(max_length=30)

    def __str__(self):
        return self.Category


class MaterialStoreIn(models.Model):
    Dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    Category = models.CharField(max_length=15)
    Subcategory_en = models.CharField(max_length=15)
    Subcategory = models.CharField(max_length=15)
    Number = models.CharField(max_length=20)
    Name = models.CharField(max_length=100)
    Specification = models.CharField(max_length=50)
    Unit = models.CharField(max_length=100)
    Quantity = models.IntegerField(default=0)
    datetime = models.CharField(max_length=30)

    def __str__(self):
        return self.Category


class MaterialStoreOut(models.Model):
    Dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    Category = models.CharField(max_length=15)
    Subcategory_en = models.CharField(max_length=15)
    Subcategory = models.CharField(max_length=15)
    Number = models.CharField(max_length=20)
    Name = models.CharField(max_length=100)
    Specification = models.CharField(max_length=50)
    Unit = models.CharField(max_length=100)
    Quantity = models.IntegerField(default=0)
    datetime = models.CharField(max_length=30)
    recipient = models.CharField(max_length=15)

    def __str__(self):
        return self.Category


class MaterialTeacher(models.Model):
    Dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Name


class StoreOutRecord(models.Model):
    Dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    OriginNumber = models.CharField(max_length=50)
    # OriginName = models.CharField(max_length=20)
    OriginQuantity = models.IntegerField(default=0)  # 原先領出數量
    OriginRecipient = models.CharField(max_length=15)
    AfterNumber = models.CharField(max_length=50)
    AfterRecipient = models.CharField(max_length=20)
    AfterQuantity = models.IntegerField(default=0)  # 後來領出數量
    Reason = models.TextField(max_length=200)
    IfDelete = models.BooleanField()  # 1是被刪 0是沒被刪
    datetime = models.CharField(max_length=30)
    editTime = models.CharField(max_length=30)

    def __str__(self):
        return self.OriginNumber
    
class StoreInRecord(models.Model):
    Dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    OriginNumber = models.CharField(max_length=50)
    # OriginName = models.CharField(max_length=20)
    OriginQuantity = models.IntegerField(default=0)  # 原先領出數量    
    AfterNumber = models.CharField(max_length=50)    
    AfterQuantity = models.IntegerField(default=0)  # 後來領出數量
    Reason = models.TextField(max_length=200)
    IfDelete = models.BooleanField()  # 1是被刪 0是沒被刪
    datetime = models.CharField(max_length=30)
    editTime = models.CharField(max_length=30)

    def __str__(self):
        return self.OriginNumber

class ThisMonthOutPut(models.Model):
    Dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    datetime = models.CharField(max_length=30)
    IfOutPut = models.BooleanField()  # 1是出單 0是未出單

    def __str__(self):
        return self.datetime


class OpenTime(models.Model):
    Dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    StartTime = models.CharField(max_length=30, default="0000/00")
    EndTime = models.CharField(max_length=30, default="0000/00")

    def __str__(self):
        return self.StartTime



'''
class InformationStock(models.Model):
    Category = models.CharField(max_length=15) 
    Subcategory_en = models.CharField(max_length=15) 
    Subcategory = models.CharField(max_length=15) 
    Number = models.CharField(max_length=20)
    Name = models.CharField(max_length=20) 
    Specification = models.CharField(max_length=50) 
    Unit = models.CharField(max_length=10) 
    Quantity = models.IntegerField(default=0)

class InformationStocklog(models.Model):
    Category = models.CharField(max_length=15) 
    Subcategory_en = models.CharField(max_length=15) 
    Subcategory = models.CharField(max_length=15) 
    Number = models.CharField(max_length=20)
    Name = models.CharField(max_length=20) 
    Specification = models.CharField(max_length=50) 
    Unit = models.CharField(max_length=20) 
    Quantity = models.IntegerField(default=0)
    datetime = models.CharField(max_length=30) 
class InformationStoreIn(models.Model):
    Category = models.CharField(max_length=15) 
    Subcategory_en = models.CharField(max_length=15) 
    Subcategory = models.CharField(max_length=15) 
    Number = models.CharField(max_length=20)
    Name = models.CharField(max_length=20) 
    Specification = models.CharField(max_length=50) 
    Unit = models.CharField(max_length=20) 
    Quantity = models.IntegerField(default=0)
    datetime = models.CharField(max_length=30)
class InformationStoreOut(models.Model):
    Category = models.CharField(max_length=15) 
    Subcategory_en = models.CharField(max_length=15) 
    Subcategory = models.CharField(max_length=15) 
    Number = models.CharField(max_length=20)
    Name = models.CharField(max_length=20) 
    Specification = models.CharField(max_length=50) 
    Unit = models.CharField(max_length=20) 
    Quantity = models.IntegerField(default=0)
    datetime = models.CharField(max_length=30) 
    recipient = models.CharField(max_length=15)
class InformationTeacher(models.Model):
    Name = models.CharField(max_length=15)
'''
# 帳號


class AccountManager(BaseUserManager):
    def create_user(self, department, username, password):
        if not username:
            raise ValueError("使用者必須有名稱")
        user = self.model(
            username=username,
            department=department,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, department, username, password):
        if not username:
            raise ValueError("使用者必須有名稱")
        user = self.create_user(
            department=department,
            username=username,
            password=password,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    # email = models.EmailField(verbose_name=email, max_length=60)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=200)
    department = models.CharField(max_length=10)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'department']

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
