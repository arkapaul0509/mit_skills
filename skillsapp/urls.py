from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login/$', views.login_request,  name='login'),
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^logout/$', views.logout_request, name='logout'),
]