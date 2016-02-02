from django.shortcuts import get_object_or_404, render
from .models import Movie

def landing_page(request):
    return render(request, "starter/landing_page.html", {'movie_list' : Movie.objects.all})
	
def movie_item(request, movie):
	return render(request, "starter/list_item.html", Movie)
	
def login(request, Movie):
	return render(request, "starter/login.html", Movie)
	
def signup(request):
	return render(request, "starter/signup.html")