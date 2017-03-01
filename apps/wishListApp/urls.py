from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^wish_items/create/$', views.create, name = 'create'),
    url(r'^newItem$', views.newItem, name = 'newItem'),
    url(r'^wish_items/(?P<id>\d+)$', views.show, name="show"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^add/(?P<id>\d+)$', views.add, name= 'add'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name= 'remove')
]
