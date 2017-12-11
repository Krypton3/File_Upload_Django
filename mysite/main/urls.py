from django.conf.urls import url

from . import views
app_name = 'main'
urlpatterns = [
    url(r'^clear/$', views.Delete_Files, name='clear_database'),
    url(r'^upload/$', views.Upload.as_view(), name='upload'),
]
