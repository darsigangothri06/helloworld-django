from django.conf import settings
from django.shortcuts import render

def index(request):
    name = request.GET.get('name')
    return render(request, 'testapp/base.html', context = {'name': name})