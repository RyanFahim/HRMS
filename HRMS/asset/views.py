from django.shortcuts import render,redirect
from .forms import AssetForm
from .models import Asset

# Create your views here.
def asset_list(request):
    context = {'asset_list': Asset.objects.all()}
    
    return render(request, 'asset_list.html',context)

def asset_form(request):
    if request.method == 'GET':   
        form = AssetForm()
        return render(request, 'asset_form.html',{'form':form})
    else:
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/asset')


def asset_delete(request,id):
    asset = Asset.objects.get(pk=id)
    asset.delete()
    return redirect('/asset')