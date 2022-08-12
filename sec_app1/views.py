from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import *
from django.contrib import messages
from datetime import datetime,timedelta,date
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator , EmptyPage
from sec_app2.models import *
from itertools import chain
# Create your views here.
def first(request):
     if request.method=='POST':
        a = request.POST['user_name']
        b = request.POST['first_name']
        c = request.POST['last_name']
        d = request.POST['email']
        e = request.POST['pasw']
        e1 = request.POST['con_pass']
        f=created(user_name=a,first_name=b,last_name=c,email=d,pasw=e,con_pass=e1)

        f.save()

        return redirect('/')

     else:
        return render(request,'first.html')
def main(request):
    if request.session.has_key('myname')and request.session.has_key('myemail'):
        user=request.session['myname']
        email=request.session['myemail']
        return render(request,'first_page.html',{'name':user})
    else:
        return render(request,'home.html')
def first1(request):
    if request.method=='POST':
        a = request.POST['user_name']
        d = request.POST['email']
        e = request.POST['pasw']
        # obj=auth.authenticate(user_name=a,email=d,pasw=e)
        obj= created.objects.filter(user_name=a,email=d,pasw=e)
        f=login(user_name=a,email=d,pasw=e)
        f.save()
        if len(obj)>0:
            for i in obj:
                user=i.user_name
                email=i.email
            request.session['myname']=user
            request.session['myemail']=email
            return redirect('main')
        else:
          return render(request,'first_log.html',{'msg':'Incorrect email id & password'})

    else:
       return render(request,'first_log.html')
def logout(request):
    del request.session['myname']
    del request.session['myemail']
    return redirect('/')

def first2(request):
    if request.method=='POST':
        a=request.POST['book_name']
        b=request.POST['author_name']
        c=request.POST['book_id']
        d=request.POST['book_category']
        # d1=request.POST['status']
        e=add_book(book_name=a,author_name=b,book_id=c,book_category=d)
        e.save()
        c=add_book.objects.all()
        return redirect('main')
        # return render(request,'first_all_book.html',{'result':c})
    else:
        return render(request,'first_add_book.html')
def first3(request):
    obj=add_book.objects.all()
    p=Paginator(obj,5)

    page_num = request.GET.get('page',1)

    try:


        page_obj = p.get_page(page_num)

    except:

        page_obj = p.get_page(1)
    return render(request,'first_all_book.html',{'result':page_obj})

def first4(request):
    obj =add_book.objects.all()
    p=Paginator(obj,5)

    page_num = request.GET.get('page',1)

    try:


        page_obj = p.get_page(page_num)

    except:

        page_obj = p.get_page(1)
    return render(request,'first_del_book.html',{'result':page_obj})


def delete(request,id):
    obj = add_book.objects.get(id = id)
    obj.delete()
    c =add_book.objects.all()
    return render(request,'first_del_book.html',{'result':c})

def issue(request):
    return render(request,'first_issue_book.html')

def first5(request):
    if request.method=='POST':
      b_name=request.POST['book_name']
      a_name=request.POST['author_name']
      b_category=request.POST['book_category']
      stu_name=request.POST['student_name']
      stu_id=request.POST['student_id']
      b_id=request.POST['book_id']
      obj=add_book.objects.filter(book_name=b_name,book_id=b_id)
      obj1=issue_books(book_name=b_name,book_id=b_id,student_id=stu_id,student_name=stu_name,author_name=a_name,book_category=b_category)
      obj1.save()
      obj.delete()
      return redirect('main') 
    else:
      return render(request,'first_issue_book.html',{'msg':'book already issued!!'})

   

def first6(request):
    c=issue_books.objects.all()
    ob=issue.objects.all()
    obj = list(chain(c, ob))
    p=Paginator(obj,5)

    page_num = request.GET.get('page',1)

    try:


        page_obj = p.get_page(page_num)

    except:

        page_obj = p.get_page(1)
  
    return render(request,'first_view_issuebook.html',{'result':page_obj})

def first7(request):
    if request.method=='POST':
      b_name=request.POST['book_name']
      stu_name=request.POST['student_name']
      stu_id=request.POST['student_id']
      b_id=request.POST['book_id']
      a_name=request.POST['author_name']
      b_category=request.POST['book_category']
      obj=issue_books.objects.filter(book_name=b_name,book_id=b_id,student_id=stu_id,student_name=stu_name)
      obj2=add_book(book_name=b_name,book_id=b_id,book_category=b_category,author_name=a_name)
      obj1=return_book(book_name=b_name,book_id=b_id,student_id=stu_id,student_name=stu_name)
      obj.delete()
      obj1.save()
      obj2.save()
      return redirect('main') 
    else:
      return render(request,'first_return_book.html')


def edit(request,id):
    obj=add_book.objects.get(id=id)
    c={
        'id':obj.id,
        'book_name':obj.book_name,
        'author_name':obj.author_name,
        'book_id':obj.book_id,
        'book_category':obj.book_category,
    }
    return render(request,'first_update_book.html',context=c)

def update(request,id):
    obj=add_book.objects.get(id=id)
    obj.book_name=request.POST['book_name']
    obj.author_name=request.POST['author_name']
    obj.book_id=request.POST['book_id']
    obj.book_category=request.POST['book_category']
    obj.save()
    c=add_book.objects.all()
    return render(request,'first_all_book.html',{'result':c})

def first8(request):
    obj=add_book.objects.all()
    p=Paginator(obj,5)

    page_num = request.GET.get('page',1)

    try:


        page_obj = p.get_page(page_num)

    except:

        page_obj = p.get_page(1)
    return render(request,'first_edit_book.html',{'result':page_obj})


def change(request):
  if request.method=='POST':
    email=request.POST['email']
    ol_pass=request.POST['old']
    new_pass=request.POST['new']
    con_pass=request.POST['conf']
    obj=signup.objects.filter(email=email,pasw=ol_pass)
    if len(obj)>0:
      if new_pass != con_pass:
        return render(request,'first_change_pass.html',{'message':'password mismatch','email':email})
      else:
        obj= signup.objects.get(email=email)
        obj.pasw=con_pass
        obj.save()
        return render(request,'first_change_pass.html',{'email':email,'message':'congrats! Password change sucessfully'})
    # return render(request,'sec_change_pass.html',{'email':email})
  else:
    return render(request,'first_change_pass.html')

def check_pass(request):
    if request.session.has_key('myname')and request.session.has_key('myemail'):
        user=request.session['myname']
        email=request.session['myemail']
        return render(request,'first_change_pass.html',{'email':email})

# def profile(request):
#    if request.session.has_key('myname')and request.session.has_key('myemail'):
#       user=request.session['myname']
#       email=request.session['myemail']
#       obj=created.objects.get(email=email)
#       c={
#       'id':obj.id,
#      'user_name':obj.user_name,
#      'first_name':obj.first_name,
#      'last_name':obj.last_name,
#      'email':obj.email,
#       }
#       return render(request,'first_profile.html',context=c)
# #   return render(request,'first_profile.html',{'res':c})
   

# def profile(request):
#    if request.session.has_key('myname')and request.session.has_key('myemail'):
#     email=request.session['myemail']
#     user=request.session['myname']
#     obj=created.objects.get(email=email)
#     c={
#         'id':obj.id,
#         'first_name':obj.first_name,
#         'last_name':obj.last_name,
#         'user_name':obj.user_name,
#         'email':obj.email,
#      }
#     return render(request,'first_profile.html',{'email':email})
#    else:
#     return render(request,'first_profile.html')

def profile(request):
    if request.session.has_key('myname')and request.session.has_key('myemail'):
       user=request.session['myname']
       email=request.session['myemail']
       obj=created.objects.get(email=email)
       c={
       'id':obj.id,
      'user_name':obj.user_name,
      'first_name':obj.first_name,
      'last_name':obj.last_name,
      'email':obj.email,
       }
    return render(request,'first_profile.html',context=c)
  



