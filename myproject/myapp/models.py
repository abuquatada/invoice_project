from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager ,PermissionsMixin


# Create your models here.



class Customers(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=255)
    ContactName = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    PostalCode = models.PositiveIntegerField(blank=False)
    Country = models.CharField(max_length=155)
    Email = models.EmailField(unique=True)
    Phone = models.CharField(max_length=20)

    DisplayField = ['CustomerID','CustomerName','ContactName','Address','City','PostalCode','Country','Email','Phone'] 

    SearchField = ['CustomerID','CustomerName']
    FilterField = ['City']

    class Meta:
        db_table = "customers"


class Products(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10,decimal_places=4)
    TaxRate = models.DecimalField(max_digits=10,decimal_places=4)
    StockQuantity = models.IntegerField()

    DisplayField = ['ProductID','ProductName','Description','Price','TaxRate','StockQuantity']

    SearchField = ['ProductID','ProductName']
    FilterField = ['Price']
    

class Invoices(models.Model):
    InvoiceID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customers,on_delete=models.SET_NULL,null=True)
    InvoiceDate = models.DateTimeField()
    DueDate = models.DateTimeField()
    TotalAmount = models.FloatField()
    Status = models.CharField(max_length=15)

    DisplayField = ['InvoiceID','CustomerID','InvoiceDate','DueDate','TotalAmount','Status']

    SearchField = ['InvoiceID','CustomerID']
    FilterField = ['Status']



class InvoiceItems(models.Model):
    InvoiceItemID = models.AutoField(primary_key=True)
    InvoiceID = models.ForeignKey(Invoices,on_delete=models.SET_NULL,null=True)
    ProductID = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    Quantity = models.IntegerField()
    UnitPrice = models.FloatField()
    TotalPrice = models.FloatField()
    TaxAmount = models.FloatField()

    DisplayField = ['InvoiceItemID','InvoiceID','ProductID','Quantity','UnitPrice','TotalPrice','TaxAmount']

    SearchField = ['InvoiceItemID','InvoiceID']
    FilterField = ['Quantity']


class Payments(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    InvoiceID = models.ForeignKey(Invoices,on_delete=models.SET_NULL,null=True)
    PaymentDate = models.DateTimeField()
    Amount = models.FloatField()
    PaymentMethod = models.CharField(max_length=55)

    DisplayField = ['PaymentID','InvoiceID','PaymentDate','Amount','PaymentMethod']

    SearchField = ['PaymentID','InvoiceID']
    FilterField = ['PaymentMethod']




class TaxRates(models.Model):
    TaxRateID = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=255)
    Rate = models.FloatField()

    DisplayField = ['TaxRateID','Description','Rate']

    SearchField = ['TaxRateID']
    FilterField = ['Description']





class UserManager(BaseUserManager):

    def create_user(self, UserName, password):
        if not UserName:
            raise ValueError('user name is required')
        
        if not password:
            raise ValueError('password is required')
        
        user = self.model(
            UserName=UserName,
        )
        user.set_password(password)

        user.save()
        return user
    

    def create_superuser(self, UserName,password,**kwargs):
        user = self.create_user(
            UserName ,password
        )

        user.is_superuser = True
        user.is_admin = True
        user.name = kwargs['name']
        # user.is_active = True
        user.is_staff = True
        # user.set_password()
        user.save()
        return user



class CoreUser(AbstractBaseUser,PermissionsMixin):
        UserID = models.AutoField(primary_key=True)
        name = models.CharField(max_length=155)
        UserName = models.CharField(max_length=255,unique=True)
        # Password = models.CharField(max_length=255)
        is_admin=models.BooleanField(default=False)
        is_staff=models.BooleanField(default=False)
        RoleID = models.ForeignKey("Role",on_delete=models.CASCADE,null=True)


        USERNAME_FIELD = 'UserName'
        REQUIRED_FIELDS = ['name']

        objects = UserManager() 



        DisplayField = ['UserID','name','UserName','RoleID']

        SearchField = ['UserID','name']
        # FilterField = ['PaymentMethod']

        class Meta:
            db_table = 'core_user'




class Role(models.Model):
     role_id=models.AutoField(primary_key=True)
     role_type = models.CharField(max_length=255)

     DisplayField = ['role_id','role_type']

     SearchField = ['role_id','role_type']
     FilterField = ['role_type']

     class Meta:
            db_table = 'role'