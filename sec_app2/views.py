from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from sec_app1.models import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, auth
from django.contrib.sessions.models import Session
from django.contrib import messages
from datetime import datetime,timedelta,date
from django.core.paginator import Paginator , EmptyPage
from itertools import chain

# Create your views here.
def student(request):
    if request.method=='POST':
        a = request.POST['user_name']
        b = request.POST['first_name']
        c = request.POST['last_name']
        c1=request.POST['roll_no']
        c2=request.POST['class_name']
        c3=request.POST['phone']
        c4=request.FILES['image']
        d = request.POST['email']
        e = request.POST['pasw']
        e1 = request.POST['con_pass']
        fs= FileSystemStorage()
        fname = fs.save(c4.name,c4)
        f= signup(user_name=a,first_name=b,last_name=c,roll_no=c1,class_name=c2,phone=c3,image=fname,email=d,pasw=e,con_pass=e1)

        f.save()

        return redirect('/')

    else:
      return render(request,'sec.html')


def main1(request):
    if request.session.has_key('myname')and request.session.has_key('myemail'):
        user=request.session['myname']
        email=request.session['myemail']
        return render(request,'sec_page.html',{'name':user})
    else:
        return render(request,'home.html')

def student1(request):
      if request.method=='POST':
        a = request.POST['user_name']
        d = request.POST['email']
        e = request.POST['pasw']
        obj= signup.objects.filter(user_name=a,email=d,pasw=e)
        f=log(user_name=a,email=d,pasw=e)
        f.save()
        if len(obj)>0:
            for i in obj:
                user=i.user_name
                email=i.email
            request.session['myname']=user
            request.session['myemail']=email
            return redirect('main1')
        else:
          return render(request,'sec_log.html',{'msg':'Incorrect email id & password'})
      else:
          return render(request,'sec_log.html')

def student2(request):
  obj=signup.objects.all()
  p=Paginator(obj,3)

  page_num = request.GET.get('page',1)

  try:


    page_obj = p.get_page(page_num)

  except:

    page_obj = p.get_page(1)
  return render(request,'sec_all_student.html',{'res':page_obj})


def student3(request):
  obj=signup.objects.all()
  p=Paginator(obj,4)

  page_num = request.GET.get('page',1)

  try:


    page_obj = p.get_page(page_num)

  except:

    page_obj = p.get_page(1)
  return render(request,'sec_del_student.html',{'res':page_obj})

def delete(request,id):
    obj = signup.objects.get(id = id)
    obj.delete()
    c =signup.objects.all()
    return render(request,'sec_del_student.html',{'res':c})


def edit(request,id):
  obj=signup.objects.get(id=id)
  c={
    'id':obj.id,
     'user_name':obj.user_name,
     'first_name':obj.first_name,
     'last_name':obj.last_name,
     'class_name':obj.class_name,
     'roll_no':obj.roll_no,
     'phone':obj.phone,
     'email':obj.email,
     'image':obj.image,
  }
  return render(request,'sec_update_student.html',context=c)

def update(request,id):
  obj=signup.objects.get(id=id)
  obj.user_name=request.POST['user_name']
  obj.first_name=request.POST['first_name']
  obj.last_name=request.POST['last_name']
  obj.class_name=request.POST['class_name']
  obj.roll_no=request.POST['roll_no']
  obj.phone=request.POST['phone']
  obj.email=request.POST['email']
  obj.image=request.FILES['image']
  fs= FileSystemStorage()
  fname = fs.save(obj.image.name,obj.image)
  obj.save()
  c=signup.objects.all()
  return render(request,'sec_all_student.html',{'res':c})

def logout(request):
  del request.session['myname']
  del request.session['myemail']
  return redirect('/')


def student4(request):
 
  if request.method=='POST':
    b_name=request.POST['book_name']
    a_name=request.POST['author_name']
    b_category=request.POST['book_category']
    stu_name=request.POST['student_name']
    stu_id=request.POST['student_id']
    email=request.POST['email']
    b_id=request.POST['book_id']
    obj=signup.objects.filter(roll_no=stu_id,first_name=stu_name)
    obj2=add_book.objects.filter(book_name=b_name,book_id=b_id)
    # obj3=issue_books.objects.get(book_name=b_name,book_id=b_id)
    obj1=issue(book_name=b_name,email=email,book_id=b_id,student_id=stu_id,student_name=stu_name,author_name=a_name,book_category=b_category)
    obj1.save()
    # obj3.save()
    obj2.delete()
    return render(request,'sec_page.html',{'email':email}) 
  else:
      return render(request,'sec_issue_book.html')

def student5(request):
  if request.session.has_key('myname')and request.session.has_key('myemail'):
    user=request.session['myname']
    email=request.session['myemail']
    obj=issue.objects.all()
    lis=[]
    li=[]
    # c={
    #   'id':obj.id,
    #   'student_name':obj.student_name,
    # }
    for i in obj:
      isdate=str(i.issued_date.day)+'-'+str(i.issued_date.month)+'-'+str(i.issued_date.year)
      exdate=str(i.expiry_date.day)+'-'+str(i.expiry_date.month)+'-'+str(i.expiry_date.year)
      print(isdate)
      print(exdate)
      days=(date.today()-i.issued_date)
      d=days.days
      fine=0
      if d>15:
        day=d-15
        fine=day*10
      print(fine)
    p=Paginator(obj,5)
    page_num = request.GET.get('page',1)
    try:
      page_obj = p.get_page(page_num)
    except:
      page_obj = p.get_page(1)
    return render(request,'sec_view_book.html',{'res':page_obj,'d':fine})
  return redirect('main1')
  

def student6(request):
  if request.method=='POST':
    b_name=request.POST['book_name']
    stu_name=request.POST['student_name']
    stu_id=request.POST['student_id']
    b_id=request.POST['book_id']
    a_name=request.POST['author_name']
    b_category=request.POST['book_category']
    obj3=signup.objects.filter(roll_no=stu_id,first_name=stu_name)
    obj=issue_book.objects.filter(book_name=b_name,book_id=b_id,student_id=stu_id,student_name=stu_name)
    obj2=add_book(book_name=b_name,book_id=b_id,book_category=b_category,author_name=a_name)
    obj1=book_return(book_name=b_name,book_id=b_id,student_id=stu_id,student_name=stu_name,book_category=b_category,author_name=a_name)
    obj.delete()
    obj1.save()
    obj2.save()
    return redirect('main1') 
  else:
      return render(request,'sec_return_book.html')

def change(request):
  # return render(request,'sec_change_pass.html')
  if request.method=='POST':
    email=request.POST['email']
    ol_pass=request.POST['old']
    new_pass=request.POST['new']
    con_pass=request.POST['conf']
    obj=signup.objects.filter(email=email,pasw=ol_pass)
    if len(obj)>0:
      if new_pass != con_pass:
        return render(request,'sec_change_pass.html',{'message':'password mismatch','email':email})
      else:
        obj= signup.objects.get(email=email)
        obj.pasw=con_pass
        obj.save()
        return render(request,'sec_change_pass.html',{'email':email,'message':'congrats! Password change sucessfully'})
    # return render(request,'sec_change_pass.html',{'email':email})
  else:
    # em=request.GET['email']
    return render(request,'sec_change_pass.html')

def check_pass(request):
    if request.session.has_key('myname')and request.session.has_key('myemail'):
        user=request.session['myname']
        email=request.session['myemail']
        obj= signup.objects.get(email=email)

        return render(request,'sec_change_pass.html',{'email':email})


def view_profile(request):
    if request.session.has_key('myname')and request.session.has_key('myemail'):
      user=request.session['myname']
      email=request.session['myemail']
      obj=signup.objects.get(email=email)
      c={
      'id':obj.id,
     'user_name':obj.user_name,
     'first_name':obj.first_name,
     'last_name':obj.last_name,
     'class_name':obj.class_name,
     'roll_no':obj.roll_no,
     'phone':obj.phone,
     'email':obj.email,
     'image':obj.image,
      }
    return render(request,'sec_profile.html',context=c)
  



   


