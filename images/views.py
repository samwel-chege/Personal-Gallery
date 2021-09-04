from django.http.response import Http404
from images.models import Images
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def image(request):
    images = Images.objects.all() 
    return render(request,"index.html",{"images":images})      