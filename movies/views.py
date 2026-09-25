from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404

from .models import Movie
from .forms import MovieForm


@login_required
def movie_list(request):
    movies = Movie.objects.filter(owner=request.user)

    return render(request, 'movies/movie_list.html', {
        'movies': movies
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie_list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {
        'form': form
    })


@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            movie = form.save(commit=False)
            movie.owner = request.user
            movie.save()

            return redirect('movie_list')
    else:
        form = MovieForm()

    return render(request, 'movies/movie_form.html', {
        'form': form
    })


@login_required
def movie_update(request, pk):
    movie = get_object_or_404(
        Movie,
        pk=pk,
        owner=request.user
    )

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)

        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movies/movie_form.html', {
        'form': form
    })


@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(
        Movie,
        pk=pk,
        owner=request.user
    )

    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')

    return render(request, 'movies/movie_confirm_delete.html', {
        'movie': movie
    })