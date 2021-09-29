from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movies
from .forms import Form


# Create your views here.
def index1(request):
    cinema = movies.objects.all()
    context = {
        'movie_list': cinema
    }

    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = movies.objects.get(id=movie_id)
    return render(request, "detail.html", {'pic': movie})


def add_movie(request):
    if request.method == 'POST':
        mname = request.POST.get('name')
        mdesc = request.POST.get('desc')
        myear = request.POST.get('year')
        mpic = request.FILES['img']
        cinemas = movies(name=mname, desc=mdesc, year=myear, img=mpic)
        cinemas.save()
    return render(request, "add.html")


def change(request, id):
    movie = movies.objects.get(id=id)
    form = Form(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        item = movies.objects.get(id=id)
        item.delete()
        return redirect('/')
    return render(request, "delete.html")
