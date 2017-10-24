from django.shortcuts import render
from jijaluka_mn import views

# Create your views here.
def index(request):
    my = {'mmm':" LOVE LOVE U U I I LOVE YOU"}
    return render(request,'index.html',context=my)
