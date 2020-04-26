from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.articles_details, name="detail"),
  #  url(r'^$',)
]
