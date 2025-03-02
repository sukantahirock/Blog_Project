from django.urls import path
from . import views
from .views import edit_post
from .views import delete_post

urlpatterns = [
    path('', views.home, name='home'),  # ✅ Home Page
    path('add/', views.add_post, name='add_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),  # ✅ Delete URL
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),

]
