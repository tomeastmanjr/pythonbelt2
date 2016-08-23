from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create$', views.create, name="create"),
    url(r'^edit/(?P<appointment_id>\d+)$', views.edit, name="edit"),
    url(r'^update/(?P<appointment_id>\d+)$', views.update, name="update"),
    url(r'^delete/(?P<appointment_id>\d+)$', views.delete, name="delete"),
    url(r'^destroy/(?P<appointment_id>\d+)$', views.destroy, name="destroy")
    ]
