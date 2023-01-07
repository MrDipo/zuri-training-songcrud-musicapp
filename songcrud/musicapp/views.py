from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html')

def create_artiste(request):
    if request.method == "POST":  
        form = ArtisteForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_artistes')  
            except:  
                pass  
    else:
        form = ArtisteForm()
        return render(request,'create_artiste.html',{'form':form}) 

def show_artistes(request):
    artistes = Artiste.objects.all()
    return render(request,"show_artistes.html",{'artistes': artistes})

def edit_artiste(request, id):
    artiste = Artiste.objects.get(id=id)
    return render(request,"edit_artiste.html", {'artiste' : artiste})  # This code might not be necessary if I can just add it to the show artiste

def update_artiste(request, id):
    artiste = Artiste.objects.get(id=id)
    form = ArtisteForm(request.POST, instance = artiste)
    if form.is_valid():
        form.save()
        return redirect("/show_artistes")
    return render(request, 'edit_artiste.html', {'artiste': artiste})  

def destroy_artiste(request, id):
    artiste = Artiste.objects.get(id=id)
    artiste.delete()
    return redirect("/show_artistes")  