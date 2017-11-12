
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),

    # /form/712/
    url(r'^(?P<form_id>[0-9]+)/$', views.detail,name='detail'),
]
