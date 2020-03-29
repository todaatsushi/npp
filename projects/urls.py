from django.urls import path

from projects import views


urlpatterns = [
    path('', views.ViewAllProjects.as_view(), name='all_projects'),
    path('<str:slug>/', views.ViewProject.as_view(), name='view_project'),
    path('<str:slug>/<int:pk>/', views.ViewPhoto.as_view(), name='view_photo'),
]
