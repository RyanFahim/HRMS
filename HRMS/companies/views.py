from django.shortcuts import render,HttpResponse, redirect
from .forms import CompanyForm
import json
from django.template.loader import render_to_string
from django.views.generic import ListView, CreateView, View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from .models import Company
from home.models import Employee
# from django.views.generic import View


class CompanyView(ListView):
    model = Company
    template_name ='company.html'
    context_object_name = 'company'


from django.views.generic import View
from django.http import JsonResponse

class CreateCompany(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        head1 = request.GET.get('head', None)
        location1 = request.GET.get('location', None)

        obj = Company.objects.create(
            name = name1,
            head = head1,
            location = location1
        )

        # user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}
        company = {'id':obj.id, 'name':obj.name, 'head':obj.head, 'location':obj.location}

        data = {
            # 'user': user
            'company':company
        }
        return JsonResponse(data)

class UpdateCompany(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        head1 = request.GET.get('head', None)
        location1 = request.GET.get('location', None)

        obj = Company.objects.get(id=id1)
        obj.name = name1
        obj.location = location1
        obj.head = head1
        obj.save()

        # user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}
        company = { 'id':obj.id, 'name':obj.name , 'head':obj.head, 'location':obj.location}

        data = {
            'company': company
        }
        return JsonResponse(data)

class DeleteCompany(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Company.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

def account(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'account.html', context)