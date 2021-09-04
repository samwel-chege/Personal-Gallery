from django.http.response import Http404
from images.models import Images
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def home(request):
    images = Images.objects.all() 
    return render(request,"index.html",{"images":images})    

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")  
        print(category)   
        searched_images = Images.search_by_category(category)
        message = f"{category}"

        return render(request,'search.html',{"message":message,"images":searched_images})

    else:
        message = "You have not searched for any term"
        return render(request,'search.html',{"message":message})    