from django.shortcuts import render

# Create your views here.
from logicapp.models import marks


def markview(request):
    data=marks.objects.all()
    return render(request,"view.html",{'data':data})
