from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import Employeeform
from .models import Employee

# Create your views here.
#admin1234, halumhalum

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")

    #Customer Table
    
    employee = Employee.objects.all()

    

    #place order table
    

    total_employee = employee.count()

    context ={
        'total_employee': total_employee

    }

    
    return render(request, 'index.html', context)

def loginUser(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')

        else:
            # No backend authenticated the credentials
            return render(request, 'loginUser.html')
            


    return render(request, 'loginUser.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render (request,'employee_list.html',context)

def employee_form(request):
    if request.method == 'GET':   
        form = Employeeform()
        return render(request, 'employee_register.html',{'form':form})
    else:
        form = Employeeform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/employee')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee')


