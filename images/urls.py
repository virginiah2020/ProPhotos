from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[
    url(r'^$',views.images,name='Images'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

