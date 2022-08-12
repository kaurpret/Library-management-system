from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
# Create your models here.

class created(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30) 
    email=models.EmailField(max_length=50)
    user_name=models.CharField(max_length=40)
    pasw=models.CharField(max_length=50)
    con_pass=models.CharField(max_length=50)
    def __str__(self):
        return self.first_name
class login(models.Model):
    user_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    pasw=models.CharField(max_length=50)
    def __str__(self):
        return self.user_name

class add_book(models.Model):
    user_name = models.ForeignKey(created,default = 1, on_delete=models.CASCADE)
    book_name=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    book_id=models.IntegerField()
    book_category=models.CharField(max_length=20)
    # status=models.CharField(max_length=100)
    def __str__(self):
        return str(self.user_name)+'['
class add_students(models.Model):
    user_name = models.OneToOneField(created, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="", blank=True)
 
    def __str__(self):
        return str(self.user_name) + " ["+str(self.branch)+']' + " ["+str(self.classroom)+']' + " ["+str(self.roll_no)+']'
def expiry():
    return datetime.today() + timedelta(days=14)
class issue_books(models.Model):
    user_name = models.ForeignKey(created,default=1,on_delete=models.CASCADE)
    student_id = models.CharField(max_length=100, blank=True) 
    book_id = models.CharField(max_length=13)
    book_name=models.CharField(max_length=20)
    author_name=models.CharField(max_length=100)
    book_category=models.CharField(max_length=20)
    student_name=models.CharField(max_length=20)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)
    def __str__(self):
        return str(self.user_name)
class return_book(models.Model):
    user_name=models.ForeignKey(created,default=1,on_delete=models.CASCADE)
    student_id = models.CharField(max_length=100, blank=True) 
    book_id = models.CharField(max_length=13)
    book_name=models.CharField(max_length=20)
    student_name=models.CharField(max_length=20)
    return_date=models.DateField(auto_now=True)
    def __str__(self):
        return self.student_id