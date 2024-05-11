from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.

def fcliente(request):

    clientes = Cliente.objects.all()
    return render(request, "cliente.html", {"clientes":clientes})

def salvar(request):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")
    if vnome:
        Cliente.objects.create(nome = vnome , telefone = vtelefone , email = vemail)
    clientes = Cliente.objects.all()
    return render(request, "cliente.html", {"clientes": clientes})

def delete(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect (fcliente)