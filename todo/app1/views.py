from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    datas = Textstore.objects.filter(isdelete=False).order_by('-id')
    if request.method=='POST':
        data= request.POST
        text = data.get('texts','')
        try:
            datas = Textstore(textmodel=text)
            datas.full_clean()
            datas.save()
            messages.success(request,'saved successfully!')
            return redirect('home')
        except Exception as e:
            messages.error(request,f'{str(e)}')
            return redirect('home')
    return render(request,'app1/home.html',{'datas':datas})

def edit(request,id):
    tasks = Textstore.objects.get(id=id)
    if request.method=='POST':
        data = Textstore.objects.get(id=id)
        data.textmodel = request.POST['texts']
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