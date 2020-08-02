from django.conf.urls import url,include
from . import viewsfrom django.conf import settings



urlpatterns=[
    url(r'^$',views.images,name='Images'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

