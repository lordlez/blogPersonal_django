from django.shortcuts import render, HttpResponse
from . models import Project




# Create your views here.
def profile(request):
    """
    p1 = Project(title="Curso de HTML", desc = "Descripción HTML")
    p1.save()

    p2 = Project(title="Curso de CSS", desc = "Descripción CSS")
    p2.save()

    p3 = Project(title="Curso de Django", desc = "Descripción Django")
    p3.save()
    """
    projects = Project.objects.all() #obtengo todos los objetos
    return HttpResponse(projects)





