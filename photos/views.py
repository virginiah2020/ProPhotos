from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def photos(request):

    photos=Photos.objects.all()
    ALLOWED_HOSTS = config('ALLOWED_HOSTS')

    return render(request,'photos.html',{"photos":images,"ALLOWED_HOSTS":ALLOWED_HOSTS})

