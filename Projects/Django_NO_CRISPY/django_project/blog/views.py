# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

#def index(request):
# # return HttpResponse("Welcome to Loonycorn")
#can also put straight html language in here and view it in the browser but best practice is to seperate html into templates
#this function will render the home.html file 
def index(request):
    return render(request, 'blog/index.html')


def business(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/business.html', context)

# Hard coded posts until we had posts in the database using the python shell
#posts = [
#{
#    'author' : 'Loonycorn',
#    'title' : 'Blog Post 1',
#    'content' : 'First post content',
#    'date_posted' : 'October 25, 2019'
#},
#{
#    'author' : 'Test',
#    'title' : 'Blog Post 2',
#    'content' : 'Second post content',
#    'date_posted' : 'October 26, 2019'
#}
#]
#
#def business(request):
#    context = {
#        'posts' : posts
#    }
#    return render(request, 'blog/business.html', context)