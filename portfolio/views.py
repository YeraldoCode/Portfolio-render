from django.shortcuts import render # type: ignore
from .models import Project



# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html" , {'projects': projects})