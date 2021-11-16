
from django.shortcuts import render

# Create your views here.
from . models import Place,foods


def demo(request):
    obj=Place.objects.all()
    ob = foods.objects.all()
    return render(request,"index.html",{'result':obj,'res':ob})

#def demo1(request):
#    ob = foods.objects.all()
 #   return render(request,"index.html",{'result':ob})
