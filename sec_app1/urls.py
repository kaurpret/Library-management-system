from  django.contrib import admin  
from django.urls import path,include
from . import views
urlpatterns=[
    path('first',views.first,name='first'),
    path('first1',views.first1,name='first1'),
    path('first2',views.first2,name='first2'),
    path('first3',views.first3,name='first3'),
    path('first4',views.first4,name='first4'),
    path('issue',views.issue,name='issue'),
    path('first5',views.first5,name='first5'),
    path('first6',views.first6,name='first6'),
    path('first7',views.first7,name='first7'),
    path('first8',views.first8,name='first8'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('logout',views.logout,name='logout'),
    path('main',views.main,name='main'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('change',views.change,name='change'),
    path('check_pass',views.check_pass,name='check_pass'),
    path('profile',views.profile,name='profile'),


]