
from django.shortcuts import render_to_response,render
from .models import Movies
from .forms import MovieForm


def home(request):
	context={
'posts' : Movies.objects.all()
}
	return render(request,'blog/home.html',context)

def add_movie(request):
    
    if request.POST:
        form = MovieForm(request.POST)
        if form.is_valid():
            # Check if the movie already exists in the database
            check_db = Movies.objects.filter(title=request.POST['title'])
            if len(check_db) > 0:
                # If a movie with same name exists the do not enter to DB
                return render(request, 'blog/movie_exists.html',
                              {'movie_title': request.POST['title']})
            else:
                # Save form and redirect to the success page
                form.save()
                return render_to_response('blog/added.html',
                                          {'movie_title': request.POST['title']})
    else:
        form = MovieForm()
    return render(request,'blog/add_movie.html',
                  {'form': form})


def search_movie(request):
	 return render(request,'blog/search_movie.html')

def list_all(request):
    """ Module to list all the movies in the database"""
    sort_by = request.GET.get('sort', 'title')
    print ("Ordering by"), sort_by
    movie_listing = []
    for movie_object in Movies.objects.all().order_by(sort_by):
        movie_dict = {'movie_object': movie_object}
        movie_listing.append(movie_dict)
    return render_to_response('blog/list_all.html', {'movie_listing': movie_listing})
	 
