from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from movil.models import Categoria,Empleado
from movil.forms import FormularioEmpleado
from django.core.mail import send_mail
import datetime

# Create your views here.
def home(request):
    return render(request,'base.html')

def categoria(request):
    return render(request,'categorias.html')
def cargo(request):
    return render(request,'cargos_trabajador.html')

def prueba(request):
    return render(request,'prueba.html')


def buscar(request):
    errors=[]
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if len(q)<1:
            errors.append('Por favor ingrese un criterio de busqueda')
        elif len(q)>20:
            errors.append('Ingrese menos de 20 digitos')
        else:
            categoria = Categoria.objects.filter(Descripcion__icontains=q)
            return render(request, 'resultados.html', {'categoria':categoria,'query':q})
    return render(request, 'formulario_buscar.html',{'errors':errors})

def Fecha_actual(request):
    ahora= datetime.datetime.now()
    return render(request, 'fecha_actual.html', {'fecha_actual':ahora})

def horas_adelante(request, horas):
    try:
        horas = int(horas)
    except ValueError:
        raise Http404()
    dt= datetime.datetime.now()+datetime.timedelta(hours=horas)
    return render(request,'horas_adelante.html',{'hora_siguiente':dt, 'horas':horas})

def empleado(request):
    if request.method=='POST':
        form=FormularioEmpleado(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            Ape=cd.get('Apellidos')
            Nom=cd.get('Nombres')
            dni=cd.get('DNI')
            dir=cd.get('Direccion')
            dist=cd.get('Distrito')
            prov=cd.get('Provincia')
            telf=cd.get('Telefono')
            corre=cd.get('Correo')
            cat=cd.get('Categoria')
            carg=cd.get('Cargo')
            est=cd.get('Estado')

            obj=Empleado.objects.create(Apellidos=Ape, Nombres=Nom,DNI=dni,Direccion=dir,Distrito=dist,
                                        Provincia=prov,Telefono=telf,Correo=corre, categorias=cat,
                                        cargos=carg,Estado=est)

            return HttpResponseRedirect('/emp/')
    else:
        form= FormularioEmpleado()

    return render(request, 'empleado.html',{'form':form})

def ListaEmpleado(request):
    lista=Empleado.objects.all()
    return render(request, 'lista_empleado.html', {'lista':lista})
