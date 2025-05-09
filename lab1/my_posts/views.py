from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound

posts = [
    {
        'id': 1,
        'title': 'The Power of Habit: How Small Changes Make a Big Impact',
        'content': 'Discover how forming small, consistent habits can lead to massive personal and professional growth. Based on behavioral psychology and real-life examples, this post explores the science behind habit formation.',
        'image': 'posts/images/image1.gif'
    },
    {
        'id': 2,
        'title': 'AI in 2025: What to Expect from the Future of Technology',
        'content': 'Artificial intelligence is evolving fast. In this article, we dive into the upcoming trends, ethical debates, and real-world applications of AI that will shape our world in 2025 and beyond.',
        'image': 'posts/images/image2.png'
    },
    {
        'id': 3,
        'title': '10 Must-Visit Hidden Gems in Europe',
        'content': 'Tired of crowded tourist spots? This travel guide lists 10 breathtaking, lesser-known destinations across Europe that offer rich culture, scenic beauty, and unforgettable experiences.',
        'image': 'posts/images/image3.png'
    }
]

# Create your views here.
def index(request):
    return render(request, "posts/index.html", context = {
        'posts': posts,
    })

def post_by_id(request, post_id):
    try:
        post_id = int(post_id)
        post = next((p for p in posts if p['id'] == post_id), None)

        if post is None:
            return HttpResponseNotFound(f"Post #{post_id} not found")

        return render(request, "posts/post.html", {
            'post': post,
        })
    except ValueError:
        return HttpResponseNotFound(f"Post #{post_id} not found")
