from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home , name='home'),
    url(r'^podcast$', views.podcast, name='podcast'),
    url(r'^post/(?P<pk>\d+)/$', views.episode, name='episode'),
    url(r'^gallery$', views.gallery , name='gallery'),
    url(r'^orderform$', views.orderform , name='orderform'),
    url(r'^about$', views.about , name='about'),
    url(r'^contact$', views.contact , name='contact'),
]
