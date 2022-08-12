from django.contrib import admin
from . models import *
# Register your models here.
class stu(admin.ModelAdmin):
    list_display = ('first_name','last_name','user_name','roll_no','class_name','phone','image','email','pasw','con_pass')
admin.site.register(signup,stu)
class stu1(admin.ModelAdmin):
    list_display = ('user_name','email','pasw')
admin.site.register(log,stu1)
class stu4(admin.ModelAdmin):
    list_display=('book_name','book_id','student_name','email','student_id','issued_date','expiry_date','book_category','author_name')
admin.site.register(issue,stu4)
class stu5(admin.ModelAdmin):
    list_display=('user_name','book_name','book_id','student_name','student_id','return_date','book_category','author_name')
admin.site.register(book_return,stu5)