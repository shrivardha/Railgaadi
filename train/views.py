from django.shortcuts import render
from django.http import HttpResponse


from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

      
def home(request):
    
    return render(request, 'train/home.html')

def about(request):
    return render(request, 'train/about.html', {'title': 'About'}) 
@login_required       
def schedule(request):
    t= Add_Train.objects.all()
    print(t)
    return render(request,'train/schedule.html',{'t':t})

@login_required
def railgaadi(request):
    return render(request,'train/railgaadi.html')


@login_required
def search(request):
    data = Add_route.objects.values('route').distinct()
    ase = Asehi.objects.all()
    coun = 0
    error=False
    fare3=0
    count = 0
    count1 = 0
    data1=0
    data2=0
    route1=[]
    route=0
    b_no =[]
    b_no1 =[]
    flag=0
    
    if request.method=="POST":
        f = request.POST["fcity"]
        t = request.POST["tcity"]
        da = request.POST["date"]
        data1 = Add_route.objects.filter(route=f)
        data2 = Add_route.objects.filter(route=t)
        for i in data1:
            for j in data2:
                if i.train.train_no==j.train.train_no:
                    route1.append(Add_Train.objects.filter(train_no=i.train.train_no))
                    
                    flag=1
        for i in data1:
            fare1=i.fare
            count+=1
            b_no.append(i.train.train_no)
        for i in data2:
            fare2 = i.fare
            count1+=1
            b_no1.append(i.train.train_no)

        fare3 = fare2-fare1
        if fare3<5 and fare3>0:
            fare3 = 5
        elif fare3<0:
            fare3 = fare3*(-1)
        elif fare3==0:
            fare3 = fare3
        route = f+" to "+t
        if flag==1:
            Asehi.objects.create(fare=fare3,train_name=data1.first(),date3=da)
        for i in ase:
            coun = coun + 1
            error=True

    d={"data2":data,'route1':route1,'fare3':fare3,"error":error,'coun':coun,'route':route}
    return render(request,'train/search.html',d)

@login_required
def Book_detail(request,coun,pid,route1):
    if not request.user.is_authenticated:
        return redirect('login')
    error = False

    try:
        data = Asehi.objects.get(id=coun)                 
    except:
        data = None
    data2 = Add_Train.objects.get(id=pid)
    user2 = User.objects.filter(username=request.user.username).get()
    user1 = User.objects.filter(username=user2).get()
    pro = Passenger.objects.filter(user=user1)
    book = Book_ticket.objects.filter(user=user1)
    total = 0
    for i in pro:
        if i.status!="set":
            total = total + i.fare
    passenger=0

    if request.method=="POST":
        f = request.POST["name"]
        t = request.POST["age"]
        da = request.POST["gender"]
        passenger = Passenger.objects.create(user=user1,train=data2,route=route1,name=f,gender=da,age=t,fare=data.fare,date1=data.date3)
        Book_ticket.objects.create(user=user1, route=route1, fare=total, passenger=passenger, date2=data.date3)

        if passenger:
            error = True
    d = {'data':data,'data2':data2,'pro':pro,'total':total,'book':book,'error':error,'route1':route1,'coun':coun,'pid':pid}
    return render(request,'train/book_detail.html',d)


@login_required
def Delete_passenger(request,pid,bid,route1):
    data = Passenger.objects.get(id=pid)
    data.delete()
    ase = Asehi.objects.all()
    coun = 7
    for i in ase:
        coun = coun + 1
    messages.info(request,'Passenger Deleted Successfully')
    return redirect('book_detail', coun,bid,route1)

def Card_Detail(request,total,coun,route1,pid):
    error=False
    try:
        data = Asehi.objects.get(id=coun)
    except:
        data=None
    data2 = Add_Train.objects.get(id=pid)
    user2 = User.objects.filter(username=request.user.username).get()
    user1 = User.objects.filter(username=user2).get()
    pro = Passenger.objects.filter(user=user1)
    book = Book_ticket.objects.filter(user=user1)
    count=0
    pro1 = 0
    if request.method == "POST":
        error=True
        for i in pro:
            count = i.name
            if i.status != "set":
                i.status="set"
                i.save()
        return redirect('my_booking')

    total1=total
    d = {'user':user1,'data':data,'data2':data2,'pro':pro,'pro1':pro1,'total':total1,'book':book,'error':error,'route1':route1,'count':count}
    return render(request,'train/card_detail.html',d)
@login_required
def my_booking(request):
    user2 = User.objects.filter(username=request.user.username).get()
    user1 = User.objects.filter(username=user2).get()
    pro = Passenger.objects.filter(user=user1)
    book = Book_ticket.objects.filter(user=user1)
    d = {'user':user1,'pro':pro,'book':book}
    
    return render(request,'train/my_booking.html',d)

@login_required
def view_ticket(request,pid):
    book = Book_ticket.objects.get(id=pid)
    d = {'book':book}
    return render(request,'train/view_ticket.html',d)

@login_required
def delete_my_booking(request,pid):
    error=False
    pro = Passenger.objects.get(id=pid)
    pro.delete()
    error=True
    d = {'error':error}
    messages.info(request,'Ticket Cancelled Successfully! ')
    return render(request,'train/cancel.html',d)




   
@login_required
def cancel(request):
    user2 = User.objects.filter(username=request.user.username).get()
    user1 = User.objects.filter(username=user2).get()
    pro = Passenger.objects.filter(user=user1)
    book = Book_ticket.objects.filter(user=user1)
    d = {'user':user1,'pro':pro,'book':book}
    return render(request,'train/cancel.html',d)