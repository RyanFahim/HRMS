from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import Employeeform, cvform
from .models import *
from companies.models import Company
from django.contrib import messages
from django import forms

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
        'total_employee': total_employee, 'total_company':total_company,
        'award_list': Award.objects.all()
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
    if request.user.is_anonymous:
        return redirect("/login")

    context = {'employee_list': Employee.objects.all()}
    return render (request,'employee_list.html',context)

def employee_form(request, id=0):

    if request.user.is_anonymous:
        return redirect("/login")

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
    if request.user.is_anonymous:
        return redirect("/login")

    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee')



#About
def about(request):
    
    return render(request,'about.html')

#training
def training(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'training.html')


def price(request):

    return render(request, 'home.html')

def communication(request):

    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        desc = request.POST.get('desc')
        contact = Contact(name = name, code = code, desc = desc)
        contact.save()
        messages.success(request, "Your messege has been noted")


    
    return render(request, 'communication.html')

def complain(request):
    if request.user.is_anonymous:
        return redirect("/login")

    datas = {'complain_list': Contact.objects.all() }

    return render(request, 'complain.html', datas )

def complain_delete(request,id):
    if request.user.is_anonymous:
        return redirect("/login")

        complain = Contact.objects.get(pk=id)
        complain.delete()
    return redirect('/complain')

def award(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == "POST":
        title = request.POST.get('title')
        name = request.POST.get('name')
        award = Award(name = name, title = title)
        award.save()
    
    contxt = {'award_list':Award.objects.all()}

    return render(request,'award.html', contxt)

def attendence(request):
    return render(request, 'attendence.html')

def empAward(request):

    awardList = {'award_list':Award.objects.all()}
    return render(request,'empAward.html',awardList)

from notice.models import Notice

def noticeEmployee(request):
    noticeList = {'notice_list': Notice.objects.all()}
    return render(request,'noticeEmployee.html',noticeList)
#CV




def cv(request):
    if request.method == 'POST':
        form = cvform(request.POST, request.FILES)

        if form.is_valid:
            form.save()

            img_obj = form.instance
            return render(request, 'cv.html', {'form': form, 'img_obj': img_obj})
    else:
        form = cvform()
    return render(request, 'cv.html', {'form': form})

def candidate(request):

    cvList = {'cv_list': CVinfo.objects.all()}
    return render(request, 'candidate.html', cvList)

def map(request):
    return render(request, 'map.html')