from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^skills/$', views.skills, name='skills'),
    url(r'^about/$', views.about, name='about'),
    url(r'^work/$', views.work, name='work'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^contact/$', views.contact, name='contact'),
]