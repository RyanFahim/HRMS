from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import Employeeform
from .models import Employee
from companies.models import Company

# Create your views here.
#admin1234, halumhalum

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")

    #Customer Table
    
    employee = Employee.objects.all()
    company = Company.objects.all()
    
    total_employee = employee.count()
    total_company = company.count()

    context ={
        'total_employee': total_employee, 'total_company':total_company
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

def employee_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = Employeeform()
        else:
            employee = Employee.objects.get(pk=id)
            form = Employeeform(instance=employee)
        return render(request, 'employee_register.html',{'form':form})
    else:
        if id == 0:
            form = Employeeform(request.POST)
        else:
            employee = Employee.objects.get(pk=id) 
            form = Employeeform(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee')


