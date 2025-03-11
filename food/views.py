from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)  
    return HttpResponse("Hello, world. I can do it")

def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def product(request):
    return HttpResponse("This is a product view")