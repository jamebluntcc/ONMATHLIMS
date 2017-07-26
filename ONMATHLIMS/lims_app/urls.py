from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'project_input/', views.project_input),
    url(r'main/', views.main, name='main'),
    url(r'receive_sample/', views.receive_sample, name='receive_sample'),
    url(r'^$', views.login, name='login'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^search/', views.search, name='search'),
    url(r'^save_sample_info', views.save_sample_info, name='save_sample_info'),
    url(r'^quality_check/', views.quality_check, name='quality_check'),
    url(r'^build_lib/', views.build_lib, name='build_lib'),
    url(r'^upmachine/', views.upmachine, name='upmachine'),
    url(r'^downmachine/', views.downmachine, name='downmachine'),
]
