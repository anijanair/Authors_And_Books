from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.author_list),
    url(r'(?P<pk>\d+)/$', views.auhtor_detail),
]