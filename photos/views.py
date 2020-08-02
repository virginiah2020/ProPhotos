from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def photos(request):

    photos=Photo.objects.all()
    ALLOWED_HOSTS = config('ALLOWED_HOSTS')

    return render(request,'photos.html',{"photos":images,"ALLOWED_HOSTS":ALLOWED_HOSTS})

# def search_results(request):
#     if 'photos' in request.GET and request.GET["photos"]:
#         search_term = request.GET.get("photos")
#         searched_photos = Photo.search_by_category(search_term)
#         message = f"{search_term}"

#         return render(request,'search.html',{"message":message,"photos":searched_images})