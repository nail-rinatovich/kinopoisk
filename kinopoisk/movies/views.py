from django.shortcuts import render
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all().order_by('-created_at')
    return render(request, 'movies/list.html', {'movies': movies})