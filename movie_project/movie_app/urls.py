from django.urls import path
from . import views
app_name = "movie_app"
urlpatterns = [
    path('', views.index, name="index"),
    path('movie/<int:movie_id>/', views.details, name="details"),
    path('add/', views.add_movie, name="add_movie"),
    path('update/<int:movie_id>/', views.update_movie, name="update_movie"),
    path('delete/<int:movie_id>', views.delete_movie, name="delete_movie"),

]
