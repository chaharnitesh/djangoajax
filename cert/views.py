from django.shortcuts import render
from .models import CertificateRecipient
from .forms import CertificateRecipientForm
from django.http import JsonResponse
# Create your views here.

def add_view(request):
    form =CertificateRecipientForm(request.POST or None,request.FILES or None)
    print(form)
    data = {}
   
    print('1111111111111111')
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data['name'] = form.cleaned_data.get('name')
            data['status']='ok'
            print('111111111111111')
            return JsonResponse(data)

    context={'form':form}
    return render(request,'qseal.html',context)
