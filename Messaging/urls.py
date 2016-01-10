from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import logout


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/whatsapp'}, name="logout"),
    url(r'^register/$', views.register, name="register"),
    url(r'^register/newusr/$', views.newusr, name="newusr"),
    url(r'^(?P<user_id>[0-9]+)/$', views.messages, name="message" ),
]
