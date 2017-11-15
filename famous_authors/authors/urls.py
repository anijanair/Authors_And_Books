from django.conf.urls import url

from . import views

#
urlpatterns = [
    url(r'^$', views.author_list, name='list'),
    url(r'(?P<author_pk>\d+)/(?P<book_pk>\d+)/$', views.book_detail, name='book'),
    url(r'(?P<pk>\d+)/$', views.author_detail, name='detail'),
]
