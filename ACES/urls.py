from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.mainPage, name='main'),
    url(r'^[0-9]',views.submit, name='submit'),
]