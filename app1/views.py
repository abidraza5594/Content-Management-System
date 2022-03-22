import re
from unicodedata import name
from django.shortcuts import render,redirect
from .models import Content,Contact
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout,authenticate 
from django.contrib.auth.models import Group
# Create your views here.
def form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincod=request.POST.get('pincod')
        content=Content(name=name,phone=phone,address=address,city=city,state=state,pincode=pincod)
        content.save()
        messages.success(request,'data submited successfully...')
        return redirect('/')


        
    return render(request,'form.html')


def login(request):
    if request.method=='POST':
            email=request.POST.get('username')
            password1=request.POST.get('password')
            user=auth.authenticate(username=email,password=password1)
            if user is not None:
                auth.login(request,user)
                return redirect('/info/')
            else:
                messages.info(request,'invalid password or username')
                return redirect('/login/') 
    else:
        return render(request,'login.html')
    
def signup(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.success(request,'Username is already Exist..')
                return redirect('/signup/')
            elif User.objects.filter(email=email).exists():
                messages.success(request,'Email is Already Exists...')
                return redirect('/signup/')
            else:
                user=User.objects.create_user(username=username,email=email,password=password,first_name=fname,last_name=lname)
                user=user.save()
                group=Group.objects.get(name='auther')
                user=group.add(group)
                messages.success(request,'successfully crated account..')
                return redirect('/signup/')
        else:
            messages.success(request,'Password Not Mach....')
            return redirect('/signup/')

    return render(request,'signup.html')


def info(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            s=request.POST.get('searc')
            s1=Content.objects.filter(name__icontains=s)
            return render(request,'info.html',{'data':s1})
        else:
            data=Content.objects.all()
            return render(request,'info.html',{'data':data})
    else:
        return redirect('/login/')

def contact(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        contact=Contact(fname=fname,lname=lname,email=email,msg=msg)
        contact.save()
        messages.success(request,'Thanxx for contact us..')
        return redirect('/contact/')
    return render(request,'contact.html')


def edit(request,id):
    ed=Content.objects.get(pk=id)
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincod=request.POST.get('pincod')
        content=Content(name=name,phone=phone,address=address,city=city,state=state,pincode=pincod,id=id)
        content.save()
        messages.success(request,'data is edited   successfully...')
        return redirect('/info/')
    return render(request,'edit.html',{'data':ed})


def delete(request,id):
    if request.method=='POST':
        d=Content.objects.get(pk=id)
        d.delete()
        messages.success(request,'delete successfully...')
        return redirect('/info/')
    return redirect('/info/')


def logOut(request):
    if request.method=='POST':
        logout(request)
        messages.success(request,'successfull logout..')
        return redirect('/')