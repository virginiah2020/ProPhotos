from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def photos(request):

    images=Image.objects.all()
    ALLOWED_HOSTS = config('ALLOWED_HOSTS')

    return render(request,'images.html',{"images":images,"ALLOWED_HOSTS":ALLOWED_HOSTS})

