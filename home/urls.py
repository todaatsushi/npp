from django.urls import path

from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),

    path('projects/', views.ViewProjects.as_view(), name='all_projects'),
    path('projects/<str:slug>/', views.ViewProject.as_view(), name='view_project'),
    path('projects/<str:slug>/<int:pk>/', views.ViewPhoto.as_view(), name='view_photo'),
]
