from django.shortcuts import render
from .models import place
from .models import team
# Create your views here.
def fun1(request):
    obj=place.objects.all
    tm = team.objects.all
    return render(request,"index.html",{'result':obj,'res':tm})



