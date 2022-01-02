from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Index Home</h1><br><a href='/shop'>Shop</a>")