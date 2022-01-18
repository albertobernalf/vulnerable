from django.shortcuts import render

# Create your views here.

from gpiozero import LED
from time import sleep

led = LED(17)


def manejoLuz(request):
    print ("hola Invoco pagina m,anejo de Luz¡")
    return render(request, "manejoLuz.html")

def prenderLuz(request):
    print ("hola voy a encender la luz¡")


    led.on()
    print("se supone encendido")
    return render(request, "manejoLuz.html")


def apagarLuz(request):
    print ("hola voy a encender la luz¡")


    led.off()
    print("se supone apagado")
    return render(request, "manejoLuz.html")
