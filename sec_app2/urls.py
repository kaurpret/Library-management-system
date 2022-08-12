from  django.contrib import admin  
from django.urls import path
from . import views
urlpatterns=[
    path('student',views.student,name='student'),
    path('student1',views.student1,name='student1'),
    path('student2',views.student2,name='student2'),
    path('student3',views.student3,name='student3'),
    path('student4',views.student4,name='student4'),
    path('student5',views.student5,name='student5'),
    path('student6',views.student6,name='student6'),
    path('main1',views.main1,name='main1'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('logout',views.logout,name='logout'),
    path('change',views.change,name='change'),
    path('check_pass',views.check_pass,name='check_pass'),
    path('view_profile',views.view_profile,name='view_profile'),
    path('delete/<int:id>', views.delete,name='delete'),

]