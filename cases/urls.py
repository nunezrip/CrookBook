from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'test/', views.test, name = 'test'),
    url(r'office/(?P<office_id>[0-9]+)/', views.office_detail, name='office_detail'),
]
