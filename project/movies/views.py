from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movies.html"


class MoviesDetailsVies(DetailView):
    model = Movie
    slug_field = "url"
    # template_name = "movies/movie_detail.html"


# Create your views here.
#class MoviesView(View):
#    """Список фильмов"""

    # здесь происходить обработка http-гет запросовов. 
    # request - это вся информация которая приходит от клиента на сервер и проложение
#    def get(self, request):
        # в этой точке из модели Movie извлекаються все данные в переменную movies
#        movies = Movie.objects.all()

        # в этой точке происходит рендер шаблона
        # в него передается request
        # ссылка на шаблон, который описывает представление на сайте
        # контекст. в контект передается словарь с ключем movie_list и значение со списком фильмов movies
#        return render(request, 'movies/movies.html', {'movie_list': movies})



