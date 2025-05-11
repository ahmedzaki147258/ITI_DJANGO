from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseNotFound
from .models import Post, Author, Comment
from rest_framework import generics
from .serializers import PostSerializer, AuthorSerializer, CommentSerializer

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", context = {
        'posts': posts,
    })

def post_by_id(request, post_id):
    post = Post.objects.filter(pk=post_id).first()
    if post is None:
        return HttpResponseNotFound(f"Post #{post_id} not found")
 
    return render(request, "posts/post.html", {
        'post': post,
        'comments': post.comments.all(),
    })

def author_profile(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if author is None:
        return HttpResponseNotFound(f"Author #{pk} not found")

    return render(request, "posts/author.html", {
        'author': author,
        'posts': author.posts.all(),
    })

def index(request):
    return HttpResponse("Hello, world. You're at the book outlet index.")


# Post Views
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response({
    #         'post': serializer.data,
    #         'comments': CommentSerializer(instance.comments.all(), many=True).data,
    #     })

# Author Views
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Comment Views
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

     
