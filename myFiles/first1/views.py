from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import EmployeeForm,AddForm
from .models import details

def home(request):
    records=details.objects.all()
    #login
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have logged in successfully!")
            return redirect('home')
        else:
            messages.success(request,"There was an error logging in. Please try again.")
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request,"You have successfully logged out.")
    return redirect('home')

def register_user(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            pd=form.cleaned_data['password1']
            user=authenticate(username=username,password=pd)
            login(request,user)
            messages.success(request,"You have been registered successfully!")
            return redirect('home')
        else:
            pass
        
        
    else:
        form=EmployeeForm()

        return render(request,'register.html',{'form':form})

    #return render(request,'register.html',{'form':form})

def display(request,pk):
    if request.user.is_authenticated:
        individual=details.objects.get(id=pk)
        return render(request,'display.html',{'individual':individual})
    else:
        messages.success(request,"You need to be logged in to view that page.!")
        return redirect('home')
    
def delete(request,pk):
    if request.user.is_authenticated:
        record=details.objects.get(id=pk)
        record.delete()
        messages.success(request,"The details have been deleted successfully.!")
        return redirect('home')
    else:
        messages.success(request,"You need to be logged in to delete records.!")
        return redirect('home')
    
def add(request):
    form=AddForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=='POST':
            if form.is_valid():
                form.save()
                messages.success(request,"Record added successfully.!")
                return redirect('home')
        return render(request,'add.html',{'form':form})
    else:
        messages.success(request,"You need to be logged in.!")
        return redirect('home')
    
def update(request,pk):
    if request.user.is_authenticated:
        record=details.objects.get(id=pk)
        form=AddForm(request.POST or None,instance=record)
    
        if form.is_valid():
            form.save()
            messages.success(request,"Record updated successfully.!!")
            return redirect('home')

        return render(request,'update.html',{'form':form})
    else:
        messages.success(request,"You need to be logged in.!")
        return redirect('home')
