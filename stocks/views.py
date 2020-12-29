#from django.urls import reverse_lazy
#from django.views.generic import ListView
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the comments index.")