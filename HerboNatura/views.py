from django.shortcuts import render
import json
from pathlib import Path
from unidecode import unidecode


def inicio(request):

    ruta_imagen = Path(__file__).resolve().parent / 'static' / 'img' / 'Inicio.png'

    contexto = {
        'nombre_tienda': 'Herbo Natura',
        'descripcion': 'El bienestar comienza con la naturaleza',
        'inicio_image_version': ruta_imagen.stat().st_mtime_ns
    }

    return render(request, 'inicio.html', contexto)


def catalogo(request):

    # Ubicación del archivo JSON
    ruta_json = Path(__file__).resolve().parent / 'data' / 'productos.json'

    # Abrir y leer el archivo
    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        productos = json.load(archivo)

    # Obtener búsqueda del usuario
    buscar = request.GET.get('buscar', '')

    productos_filtrados = []

    # Filtrar productos
    for producto in productos:

        nombre = unidecode(producto['nombre'].lower())
        busqueda = unidecode(buscar.lower())

        if busqueda in nombre:
            productos_filtrados.append(producto)

    # Contar productos disponibles
    disponibles = 0

    for producto in productos:
        if producto['stock'] > 0:
            disponibles += 1

    contexto = {
        'productos': productos_filtrados,
        'disponibles': disponibles,
        'buscar': buscar
    }

    return render(request, 'catalogo.html', contexto)

def nosotros(request):

    contexto = {
        'nombre_tienda': 'Herbo Natura',
        'mision': 'Acercar las propiedades tradicionales de las plantas naturales a las personas.',
        'vision': 'Promover el bienestar y el conocimiento de las hierbas naturales.'
    }

    return render(request, 'nosotros.html', contexto)

def contacto(request):

    contexto = {
        'nombre_tienda': 'Herbo Natura',
        'correo': 'contacto@herbonatura.cl',
        'mensaje': 'Estamos aquí para orientarte sobre nuestros productos naturales.'
    }

    return render(request, 'contacto.html', contexto)


