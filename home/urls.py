from django.urls import path

from home import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),

    path('projects/', views.ViewAllProjects.as_view(), name='all_projects'),
    path('projects/<str:slug>/', views.ViewProject.as_view(), name='view_project'),
    path('projects/<str:slug>/<int:pk>/', views.ViewPhoto.as_view(), name='view_photo'),
]
