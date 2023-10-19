from django.shortcuts import render 
from django.http import HttpResponse 
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request): 
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    #mydata = Member.objects.all()
    mydata = Member.objects.all().values() # Método values
    #mydata = Member.objects.values_list('firstname') # Método values_list, devuelve columnas específicas
    #mydata = Member.objects.filter(firstname='Angel').values() # Método filter, devuelve filas específicas
    #mydata = Member.objects.filter(firstname='Angel').values() # Devuelve solo las filas que coinciden con el término de búsqueda
    #mydata = Member.objects.filter(lastname='Refsnes', id=2).values() # Se puede filtrar en más de un campo separándolos por una coma
    #mydata = Member.objects.filter(firstname='Angel').values() | Member.objects.filter(firstname='Tobias').values() # Se pueden combinar varios filtros con el operador |
    #mydata = Member.objects.filter(Q(firstname='Angel') | Q(firstname='Tobias')).values() # Se pueden combinar varios filtros con el operador Q
    #mydata = Member.objects.filter(firstname__startswith='A').values() # Se pueden usar comodines para buscar coincidencias
    #mydata = Member.objects.all().order_by('firstname').values() # Se pueden ordenar los resultados con el método order_by
    #mydata = Member.objects.all().order_by('-firstname').values() # Se pueden ordenar los resultados con el método order_by, el signo - invierte el orden
    #mydata = Member.objects.all().order_by('lastname', '-id').values() # Para ordenar por más de un campo, separe los nombres de los campos con una coma en el método order_by

    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))