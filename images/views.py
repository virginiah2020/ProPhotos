from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
# from .models import Image


# Create your views here.
def images(request):

    # images=Image.objects.all()
    # ALLOWED_HOSTS = config('ALLOWED_HOSTS')

    return render(request,'photos.html',{"images":images})

# def search_results(request):
#     if 'photos' in request.GET and request.GET["photos"]:
#         search_term = request.GET.get("photos")
#         searched_photos = Photo.search_by_category(search_term)
#         message = f"{search_term}"

#         return render(request,'search.html',{"message":message,"photos":searched_images})