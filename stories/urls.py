from django.conf.urls import url
from . import views

app_name = "story"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^register/', views.user_registration, name='register'),
    url(r'^dash/', views.user_dashboard, name='dash'),
    url(r'^create/', views.create_profile, name='create'),
    url(r'^editprofile/$', views.edit_profile, name='pedit'),
    url(r'^resources/$', views.resources_dashboard, name='resources_dashboard'),
    url(r'^(?P<resource_id>[0-9]+)/editresource/$', views.edit_resource, name='edit_resource'),
    url(r'^(?P<album_id>[0-9]+)/deleteresource/$', views.delete_resource, name='delete_resource'),

]
