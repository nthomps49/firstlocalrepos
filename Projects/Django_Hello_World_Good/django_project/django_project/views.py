from django.http import HttpResponse #formats view in HttpResponse

def index(request):
    return HttpResponse("Hello world")