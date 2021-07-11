from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Genre, Movie, MovieShots, Actor, ActorTypes, Rating, RatingStar, Reviews


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("id", "name")


#class ReviewInline(admin.StackedInline):
class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("email", "name")


#class MovieShotsInline(admin.StackedInline):
class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50">')

    get_image.short_description = "Изображение"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "year", "category", "url", "draft")
    list_display_links = ("id", "title")
    list_filter = ("category", "draft", "year")
    search_fields = ("title", "category__name")
    inlines = [ReviewInline, MovieShotsInline]
    save_on_top = True
    save_as = True
    readonly_fields = ("get_poster", )
    list_editable = ("draft", )
    # fields = (("actors", "directors", "genres"), )
    fieldsets = (
        ("Общее", {
            "fields": (("title", "tagline",), ("category", "url", "draft"),)
        }),
        (None, {
            "fields": (("poster", "get_poster", ),)
        }),
        (None, {
            "fields": (("description",),)
        }),
        (None, {
            "fields": (("world_premiere", "year", "country"),)
        }),
        ("Актеры, режисеры и жанры", {
            "classes": ("collapse", ),
            "fields": (("directors", "actors", "genres"),)
        }),
        ("Финансы", {
            "classes": ("collapse", ),
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
    )

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50">')

    get_poster.short_description = " "


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "parent", "movie")
    readonly_fields = ("name", "email")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "actor_type", "get_image")
    list_display_links = ("id", "name", )
    list_filter = ("actor_type", )
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50">')

    get_image.short_description = "Изображение"

# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Movie)
# admin.site.register(Reviews)
# admin.site.register(Actor)


admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(ActorTypes)


admin.site.site_title = "Django Movies"
admin.site.site_header = "Django Movies"