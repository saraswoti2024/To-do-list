from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from datetime import date,datetime
from django.utils import timezone 
import time
import logging ##logger

logger = logging.getLogger('django')

# Create your views here.
def home(request):
    try:
        datas = Textstore.objects.filter(isdelete=False).order_by('-date','-time')
        if request.method=='POST':
            data= request.POST
            text = data['texts']
            dates = timezone.now().date()
            times = timezone.now().time()
            try:
                datas = Textstore(textmodel=text,date=dates,time=times)
                datas.full_clean()
                datas.save()
                messages.success(request,'saved successfully!')
                return redirect('home')
            except Exception as e:
                messages.error(request,f'{str(e)}')
                return redirect('home')
    except Exception as e:
        logger.error(str(e),exc_info=True)

    context={
        'datas': datas,
    }
    return render(request,'app1/home.html',context)

def edit(request,id):
    try:
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
    except Exception as e:
        logger.error(str(e),exc_info=True)
    return render(request,'app1/edit.html',{'tasks':tasks})

def delete(request,id):
    try:
        data = Textstore.objects.get(id=id)
        data.isdelete = True
        data.save()
    except Exception as e:
        logger.error(str(e),exc_info=True)
    return redirect('home')

def complete(request):
    try:
        data = Textstore.objects.filter(isdelete=True).order_by('-date','-time')
    except Exception as e:
        logger.error(str(e),exc_info=True)
    return render(request,'app1/complete.html',{'data': data})

def deletes(request,id):
    try:
        data = Textstore.objects.get(id=id)
        data.delete()
        value = request.GET.get('next')
    except Exception as e:
        logger.error(str(e),exc_info=True)
    return redirect(value)