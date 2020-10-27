# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.dates import YearArchiveView
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

class PostListView(ListView):
    model = Post
    template_name = 'blog/business.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(CreateView):
    model = Post
    fields =['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields =['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
                return True
        return False
    
class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
                return True
        return False
    
class PostYearArchiveView(YearArchiveView):
    queryset = Post.objects.all()
    date_field = "date_posted"
    make_object_list = True
    allow_future = True
    
def about(request):
    return render(request, 'blog/about.html')


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