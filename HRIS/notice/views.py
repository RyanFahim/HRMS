from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, View, DetailView
from .models import Notice

class NoticeView(ListView):
    model = Notice
    template_name = 'notice.html'
    context_object_name = 'notice'

class CreateNotice(View):
    def  get(self, request):
        title1 = request.GET.get('title', None)
        date1 = request.GET.get('date',None)
        des1 = request.GET.get('des', None)

        obj = Notice.objects.create(
            title =title1, date = date1, des=des1
        )

        notice = { 'title':obj.title, 'date':obj.date, 'des':obj.des }

        data = {
            'notice':notice
        }

        return JsonResponse(data)


class DeleteNotice(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Notice.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class UpdateNotice(View):
    def  get(self, request):
        id1 = request.GET.get('id',None)
        title1 = request.GET.get('title',None)
        date1 = request.GET.get('date', None)
        des1 = request.GET.get('des', None)

        obj = Notice.objects.get(id=id1)
        obj.title = title1
        obj.date = date1
        obj.des = des1
        obj.save()


        # user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}
        notice = { 'title':obj.title , 'date':obj.date, 'des':obj.des }
        data = {
            'notice':notice
        }
        return JsonResponse(data)