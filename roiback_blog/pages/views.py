from django.shortcuts import render
from posts.models import Post
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

def home(request):
    posts = Post.objects.order_by('-publish_date')
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)
    data = {
        'posts': paged_post,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
