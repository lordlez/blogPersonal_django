from django.http import HttpResponse

def hola(request):
    numeros = [int(n) for n in request.GET['numeros'].split(',')]
    print(numeros)
    numeros_ordenados = sorted(numeros)
    print(numeros_ordenados)
    print(request.GET)
    return HttpResponse(str(numeros_ordenados))


def verificar(request, nombre, edad):
    if edad < 12:
        mensaje = f'Hola, {nombre} NO PUEDE ingresar'
    else:
        mensaje = f'Hola, {nombre} PUEDE ingresar'
    
    return HttpResponse(mensaje)

