from django.contrib import admin

# Register your models here.

from .models import Movie, Actor, ReleaseDate, Poster, Rating, Character, AlternateID, User, Recommendation

class ReleaseDateInline(admin.TabularInline):
	model = ReleaseDate
	extra = 3

class PosterInline(admin.TabularInline):
	model = Poster
	extra = 3

class RatingInline(admin.TabularInline):
	model = Rating
	extra = 3
	
class CharacterInline(admin.TabularInline):
	model = Character
	verbose_name = "Character"
	verbose_name_plural = "Characters"
	list_filter = ("movie.title")
	extra = 3
	
class AlternateIDInline(admin.TabularInline):
	model = AlternateID
	extra = 3

class MovieAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['id', 'title']}),
        ('Release', {'fields': ['year'], 'classes': ['collapse']}),
		('Details', {'fields': ['mpaa_rating', 'runtime', 'synopsis'], 'classes': ['collapse']}),
    ]
	inlines = [ReleaseDateInline, PosterInline, RatingInline, CharacterInline, AlternateIDInline]
	list_display = ('id', 'title', 'year', 'mpaa_rating', 'runtime', 'synopsis')
	
class ActorAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['id', 'name']}),
    ]
	inlines = [CharacterInline]
	list_display = ('id', 'name')
	
class RecommendationInline(admin.TabularInline):
	model = Recommendation
	fk_name = 'to_user'
	extra = 3
	
class UserAdmin(admin.ModelAdmin):
	fieldsets = [ (None,	{'fields': ['name', 'role']}), ]
	inlines = [RecommendationInline]
	list_display = ('name', 'role')
	
	
admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Recommendation)