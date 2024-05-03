from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.


def index(request):
    movie = Movie.objects.all()
    return render(request, "index.html", {'movie': movie})


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "details.html", {'movie': movie})


def add_movie(request):
    if request.method == "POST":
        title = request.POST.get('title',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        movie = Movie(title=title, desc=desc, release_year=year, img=img)
        movie.save()
        return redirect('/')
    return render(request, 'add_movie.html')


def update_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "edit.html", {'form': form, 'movie': movie})


def delete_movie(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    return render(request, "delete.html")
