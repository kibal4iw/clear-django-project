from django.contrib import admin
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


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "year", "category", "url", "draft")
    list_display_links = ("id", "title")
    list_filter = ("category", "draft", "year")
    search_fields = ("title", "category__name")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft", )
    # fields = (("actors", "directors", "genres"), )
    fieldsets = (
        ("Общее", {
            "fields": (("title", "tagline",), ("category", "url", "draft"),)
        }),
        (None, {
            "fields": (("poster", "description",),)
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


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "parent", "movie")
    readonly_fields = ("name", "email")

# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Movie)
# admin.site.register(Reviews)


admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(ActorTypes)