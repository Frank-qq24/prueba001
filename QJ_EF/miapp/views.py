from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from miapp.models import curso
from miapp.models import producto

def integrantes(request):
    integrantes = ['Julca Espillco Humberto','Quintana Quispe Frank']
    return render(request, 'integrantes.html', {
        'titulo':'Integrantes del proyecto',
        'integrantes':integrantes
    })

def saludo(request):
    return render(request, 'saludo.html', {
        'titulo':'Bienvenidos a la UNTELS',
        'mensaje':'Proyecto para Examen Final'
    })

def crear_producto(request):
    productos=producto(
    codigo          = "3",
    nombre          = "ticotico",
    precio_compra   = "4",
    precio_venta    = "3",
    Fecha_compra    ="03/08/22",
    Fecha_registro = f" {datetime.today().strftime('%Y-%m-%d')}",
    estado   = "A"
    )
    productos.save()

    return render(request, 'crear_producto.html', {
        'titulo':'Crear producto',
        'producto':
        f"Producto registrado:"+
        f"//codigo: {productos.codigo} // nombre: {productos.nombre} // precio_compra: {productos.precio_compra} //"+
        f"precio_venta: {productos.precio_venta} // Fecha_compra: {productos.Fecha_compra} // Creditos: {productos.Fecha_registro}"+
        f"// Estado:{productos.estado}"
    })

def crear_curso(request):
    cursos =curso(
    codigo          = "1",
    nombre          = "algoritmo",
    horas           = "4",
    creditos        = "3",
    Fecha_registro = f" {datetime.today().strftime('%Y-%m-%d')}",
    estado          = "A"
    )
    cursos.save()

    return render(request, 'crear_curso.html', {
        'titulo':'Crear producto',
        'curso':
        f"Curso registrado:"+
        f"//codigo: {cursos.codigo} // nombre: {cursos.nombre} // precio_compra: {cursos.horas} //"+
        f"Creditos: {cursos.creditos} // Fecha_registro: {cursos.Fecha_registro}"+
        f"// Estado:{cursos.estado}"
    })