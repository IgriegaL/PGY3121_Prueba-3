from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from basedatos.models import producto, pedido, detallePedido, tipoPedido, estadoPedido, estadoEntrega, cliente, giro, proveedor, usuario


def inicio(request):
    user = ""
    pwd = ""
    mensaje = ""
    llamadabd = []
    try:
        user = request.GET["correo"]
        pwd = request.GET["password"]
        llamadabd = usuario.objects.filter(nombreUsuario__icontains=user, password__icontains=pwd)
        print(llamadabd[0].nombreUsuario)
        print(llamadabd[0].password)
        mensaje = f'Ha iniciado sesión el usuario {user}'
    except:
        mensaje = f'Los datos ingresados son inválidos, por favor intente nuevamente'
        
    contexto = {'llamadabd':llamadabd,
                'mensaje':mensaje,
                'user':user}
    
    return render(request, "index.html",contexto)


def productos(request):
    user = ""
    pwd = ""
    mensaje = ""
    llamadabd = []
    try:
        user = request.GET["correo"]
        pwd = request.GET["password"]
        llamadabd = usuario.objects.filter(nombreUsuario__icontains=user, password__icontains=pwd)
        print(llamadabd[0].nombreUsuario)
        print(llamadabd[0].password)
        mensaje = f'Ha iniciado sesión el usuario {user}'
    except:
        mensaje = f'Los datos ingresados son inválidos, por favor intente nuevamente'
    
    llamadabd = producto.objects.all()
    contexto = {'datos': llamadabd,
                'llamadabd':llamadabd,
                'mensaje':mensaje,
                'user':user
                }
    return render(request, "productos.html", contexto)

def seguimiento(request):
    return render(request, "seguimiento.html")

def donacion(request):
    return render(request, "donacion.html")

def carritoCompra(request):
    return render(request, "carritoCompra.html")



def verTablas(request):

    llamadabd1 = producto.objects.filter(id__icontains="")
    llamadabd2 = pedido.objects.filter(id__icontains="")
    llamadabd3 = detallePedido.objects.filter(id__icontains="")
    llamadabd4 = tipoPedido.objects.filter(id__icontains="")
    llamadabd5 = estadoPedido.objects.filter(id__icontains="")
    llamadabd6 = estadoEntrega.objects.filter(id__icontains="")
    llamadabd7 = cliente.objects.filter(id__icontains="")
    llamadabd8 = giro.objects.filter(id__icontains="")
    llamadabd9 = proveedor.objects.filter(id__icontains="")
    llamadabd10 = usuario.objects.filter(id__icontains="")
    contexto = {'tabla1':llamadabd1,
                'tabla2':llamadabd2,
                'tabla3':llamadabd3,
                'tabla4':llamadabd4,
                'tabla5':llamadabd5,
                'tabla6':llamadabd6,
                'tabla7':llamadabd7,
                'tabla8':llamadabd8,
                'tabla9':llamadabd9,
                'tabla10':llamadabd10,
                }

    return render(request,"verTablas.html",contexto)
