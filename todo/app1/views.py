from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from datetime import date,datetime
from django.utils import timezone 
import time

# Create your views here.
def home(request):
    datas = Textstore.objects.filter(isdelete=False).order_by('-id')
    dates = timezone.now().date()
    times = timezone.now().time()
    if request.method=='POST':
        data= request.POST
        text = data['texts']
        try:
            datas = Textstore(textmodel=text,date=dates,time=times)
            datas.full_clean()
            datas.save()
            messages.success(request,'saved successfully!')
            return redirect('home')
        except Exception as e:
            messages.error(request,f'{str(e)}')
            return redirect('home')
    context={
        'datas': datas,
    }
    return render(request,'app1/home.html',context)

def edit(request,id):
    tasks = Textstore.objects.get(id=id)
    dates = timezone.now().date()
    times = timezone.now().time()
    if request.method=='POST':
        data = Textstore.objects.get(id=id)
        data.textmodel = request.POST['texts']
        data.date = dates
        data.time = times
        try:
            data.full_clean()
            data.save()
            messages.success(request,'updated successfully')
            return redirect('home')
        except Exception as e:
            messages.error(request,f'{str(e)}')
            return redirect('edit')
    return render(request,'app1/edit.html',{'tasks':tasks})

def delete(request,id):
    data = Textstore.objects.get(id=id)
    data.isdelete = True
    data.save()
    return redirect('home')

def complete(request):
    data = Textstore.objects.filter(isdelete=True).order_by('-id')
    return render(request,'app1/complete.html',{'data': data})