from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie
from .forms import ReviewForm


class MoviesView(ListView):
    """ Список фильмов """
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movies.html"


class MoviesDetailsVies(DetailView):
    """ Детали фильма """
    model = Movie
    slug_field = "url"
    # template_name = "movies/movie_detail.html"


class AddReview(View):
    """ Добавление отзыва """
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            # form.movie_id = pk
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()

        return redirect(movie.get_absolute_url())

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



