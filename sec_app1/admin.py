from django.contrib import admin
from . models import *
# Register your models here.
class stu(admin.ModelAdmin):
    list_display = ('first_name','last_name','user_name','email','pasw','con_pass')
admin.site.register(created,stu)
class stu1(admin.ModelAdmin):
    list_display = ('user_name','email','pasw')
admin.site.register(login,stu1)
class stu2(admin.ModelAdmin):
    list_display=('user_name','book_name','author_name','book_id','book_category')
admin.site.register(add_book,stu2)
class stu3(admin.ModelAdmin):
    list_display=('user_name','classroom','branch','roll_no','phone','image')
admin.site.register(add_students,stu3)
class stu4(admin.ModelAdmin):
    list_display=('user_name','book_name','book_id','student_name','student_id','issued_date','expiry_date','book_category','author_name')
admin.site.register(issue_books,stu4)
class stu5(admin.ModelAdmin):
    list_display=('user_name','book_name','book_id','student_name','student_id','return_date')
admin.site.register(return_book,stu5)