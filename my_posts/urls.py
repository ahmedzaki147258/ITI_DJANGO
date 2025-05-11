from django.urls import path
from . import views
from .views import (
    PostListCreateView,
    PostRetrieveUpdateDeleteView,
    AuthorListCreateView,
    AuthorRetrieveUpdateDeleteView,
    CommentListCreateView,
    CommentRetrieveUpdateDeleteView,
)

urlpatterns = [
    path('', views.index, name='posts_index'),
    path('<int:post_id>', views.post_by_id),
    path('author/<int:pk>', views.author_profile),

    path('api/posts', PostListCreateView.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>', PostRetrieveUpdateDeleteView.as_view(), name='post-detail'),

    path('api/authors', AuthorListCreateView.as_view(), name='author-list-create'),
    path('api/authors/<int:pk>', AuthorRetrieveUpdateDeleteView.as_view(), name='author-detail'),

    path('api/comments', CommentListCreateView.as_view(), name='comment-list-create'),
    path('api/comments/<int:pk>', CommentRetrieveUpdateDeleteView.as_view(), name='comment-detail'),
]
