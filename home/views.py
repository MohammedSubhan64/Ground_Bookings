from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from datetime import datetime, time
from home.models import Bookings, Contact,CricketTiming
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")
    # return HttpResponse("home page")
def about(request):
     return render(request,"about.html")
def services(request):
     return render(request,"services.html")
def football(request):
    return render(request,"football.html")
def footballg1(request):
    tim=CricketTiming.objects.all()
    return render(request,"footballground1.html",{'time':tim})
def footballg2(request):
    return render(request,"footballground2.html")
def footballg3(request):
    return render(request,"footballground3.html")
def footballg4(request):
    return render(request,"footballground4.html")

def cricket(request):
       return render(request,"cricket.html")
def cricketg1(request):
       return render(request,"cricketg1.html")
def cricketg2(request):
       return render(request,"cricketg2.html")
def cricketg3(request):
    return render(request,"cricketg3.html")
def cricketg4(request):
   return render(request,"cricketg4.html")

def contact(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        des =request.POST.get('des')
        contact = Contact( name=name, email=email, phone=phone,
         des=des, date=datetime.today())
        contact.save()
        messages.success(request,'your message has been sent!')
    return render(request,"contact.html")

def groundbase(request):
       tim=CricketTiming.objects.all()
       if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        number =request.POST.get('number')
        date =request.POST.get('date')
        time =request.POST.get('time')
        groundtype=request.POST.get('groundtype')
        selectground=request.POST.get('selectground')
        groundbase = Bookings( name=name, email=email,number=number ,
        date=date , time=time, groundtype=groundtype, selectground=selectground )
        groundbase.save()
        messages.success(request,'Ground Booked Successfully!')
        return render(request,"groundbase.html",{'time':tim})
 
# # to search a venue by name    
# def search_ground(request):
#       if request.method == "POST":
#             searched =request.POST['searched']
#             search_ground =Bookings.objects.filter(name__contains=searched)
#             return render(request,'search_ground.html',{'searched':searched,'search_ground':search_ground})
       