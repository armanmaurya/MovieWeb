from django.shortcuts import render
from .models.Links import Link


# Create your views here.

def index(request):
    Links = Link.objects.all()
    Moviename = request.GET.get('MovieName')
    if Moviename:
        pass
    else:
        pass

    name = {}
    name['Movie_name'] = Links







    return render(request, 'index.html', name)


def videos(request):



    Links = Link.objects.all()

    url = {}
    url['links'] = Links

    return render(request, 'video.html', url)
