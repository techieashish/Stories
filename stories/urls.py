from django.conf.urls import url
from . import views

app_name = "story"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^register/', views.user_registration, name='register'),

]
