
from django.db import models
from django.contrib.auth.models import User
from typing_extensions import Self
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


# Create your models here.



class SignupModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    contact=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    confirmpassword=models.CharField(max_length=200)


class LoginModel(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class ContactusModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    mobileno=models.IntegerField()
    message=models.TextField(max_length=200)


class OrderModel(models.Model):
    id=models.AutoField(primary_key=True)
    orderid=models.IntegerField()
    mobileno=models.IntegerField()
    name=models.CharField(max_length=200)
    address=models.TextField(max_length=200)
    pincode=models.IntegerField()
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


     



class OrdertableModel(models.Model):
    id=models.AutoField(primary_key=True)
    orderid=models.IntegerField()
    mobileno=models.IntegerField()
    name=models.CharField(max_length=200)
    address=models.TextField(max_length=200)
    pincode=models.IntegerField()
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    


'''class Name(models.Model):
    name = models.CharField(max_length=100)
    code = models.ImageField(blank=True, upload_to='code')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.name)
        qr_offset = Image.new('RGB',(310, 310), 'white')
        qr_offset.paste(qr_image)
        files_name = f'{self.name}-{self.id}qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.code.save(files_name, File(stream),  save=False)
        qr_offset.close()
        super().save(*args, **kwargs)'''

class Ordersqr(models.Model):
    name = models.CharField(max_length=100)
    code = models.ImageField(blank=True, upload_to='code')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.name)
        qr_offset = Image.new('RGB',(310, 310), 'white')
        qr_offset.paste(qr_image)
        files_name = f'{self.name}-{self.id}qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.code.save(files_name, File(stream),  save=False)
        qr_offset.close()
        super().save(*args, **kwargs)




    