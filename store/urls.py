from django.urls import re_path

from . import views # import views so we can use them in urls.


urlpatterns = [
    re_path(r'^$', views.listing), # "/store" will call the method "index" in "views.py"
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail),
    re_path(r'^search/$', views.search),
]