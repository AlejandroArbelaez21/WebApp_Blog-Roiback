from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


def post_detail(request, id):
    single_post = get_object_or_404(Post, pk=id)

    data = {
        'single_post': single_post, 
    }
    return render(request, 'posts/post_detail.html', data)

def search(request):
    posts = Post.objects.order_by('-publish_date')
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            posts = posts.filter(categories__icontains=keyword)

    data = {
        'posts': posts,
    }
    return render(request, 'posts/search.html', data)

def delete(request):
    print(post_detail(request, 2))
    return render(request, 'posts/post_confirm_delete.html')

def confirm_delete(request, id):
    print(post_detail())