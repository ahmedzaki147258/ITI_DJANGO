from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='posts_index'),
    path('<int:post_id>', views.post_by_id),
    path('author/<int:pk>', views.author_profile),
]
