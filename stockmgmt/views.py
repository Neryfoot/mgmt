from django.shortcuts import render, redirect
from .models import *
from .forms import StockCreateForm

def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
    "title": title,
    }
    return render(request, "home.html",context)

def list_item(request):
    title = 'List of Items'
    queryset = Stock.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "list_item.html", context)

def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/add_item')
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_item.html", context)