from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseNotFound
from .models import Post, Author

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
