from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[
    url(r'^$',views.images,name='Images'),
    url(r'^search/',views.search_results, name='search_results'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

