"""lista URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from movil.views import home, Fecha_actual, horas_adelante, buscar, empleado,ListaEmpleado, categoria, cargo, prueba
from contactos.views import Index, contactos
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.Index),
    url(r'^index/$', Index, name='index'),
    url(r'^buscar/$', buscar),
    url(r'^emp/$', ListaEmpleado,name='ver_lista'),
    url(r'^contactos/$', contactos),
    url(r'^registrar/$', empleado, name='registrar'),
    url(r'^fecha/$', Fecha_actual),
    url(r'^fecha/mas/(\d{1,2})/$', horas_adelante),
    url(r'^categoria/$', categoria, name='categoria'),
    url(r'^home/$', home, name='home'),
    url(r'^cargos/$',cargo, name='cargo'),
    url(r'^prueba/$',prueba, name='prueba')
]
