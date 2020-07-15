from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello from Blog')

def post(request):
    return HttpResponse('Post a Blog')

def list_post(request):
    return HttpResponse('List of All Blog Post')