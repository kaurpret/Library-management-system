from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
import time
# Create your views here.
def home(request):
  while True:
    x=datetime.now()
    c=x.strftime('%a')
    c1=x.strftime('%d-%m-%Y')
    c2=x.strftime('%I:%M %p')
    
    return render(request,'home.html',{'res':c,'res1':c1,'res2':c2})
    # time.sleep(1)
    # import time
  # import time
  # while True:
  #   from datetime import datetime
  #   now = datetime.now()  
  #   c=(" %s:%s:%s" % (now.hour,now.minute,now.second)) 
  #   print(c)
  #   return render(request,'home.html',{'res':c})

  #   time.sleep(1)