from django.shortcuts import render
from .models import Food, Category
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'GET' :
        return render(request, 'cafe/index.html')   
 
    elif request.method == 'POST' :
        category = Category.objects.get(name=request.POST['category'])

        food_name = request.POST['menu']
        food_price = request.POST['price']
        food_description = request.POST['description']
        Food.objects.create(name = food_name, price = food_price, description = food_description, category=category)
        
        return render(request, 'cafe/index.html')

