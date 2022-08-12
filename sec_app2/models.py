from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
# Create your models here.

class signup(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    user_name=models.CharField(max_length=30)
    roll_no=models.IntegerField()
    class_name = models.CharField(max_length=10)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="", blank=True)
    email=models.EmailField(max_length=50)
    pasw=models.CharField(max_length=50)
    con_pass=models.CharField(max_length=50)
    def __str__(self):
        return self.first_name
class log(models.Model):
    user_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    pasw=models.CharField(max_length=50)
    def __str__(self):
        return self.user_name
def expiry():
    return datetime.today() + timedelta(days=14)
class issue(models.Model):
    # user_name = models.ForeignKey(signup,default=1,on_delete=models.CASCADE)
    student_id = models.CharField(max_length=100, blank=True) 
    book_id = models.CharField(max_length=13)
    book_name=models.CharField(max_length=20)
    author_name=models.CharField(max_length=100)
    book_category=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    student_name=models.CharField(max_length=20)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)
    def __str__(self):
        return str(self.student_name)
class book_return(models.Model):
    user_name = models.ForeignKey(signup,default=1,on_delete=models.CASCADE)
    student_id = models.CharField(max_length=100, blank=True) 
    book_id = models.CharField(max_length=13)
    book_name=models.CharField(max_length=20)
    student_name=models.CharField(max_length=20)
    return_date=models.DateField(auto_now=True)
    author_name=models.CharField(max_length=100)
    book_category=models.CharField(max_length=20)
    def __str__(self):
        return self.user_name

