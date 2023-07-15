from django.shortcuts import render
from .models import Posts,postCategory
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def post_list(request):
    post_list=Posts.objects.all()
    post_category=postCategory.objects.all()

    ## search 
    search_query = request.GET.get('q')
    if search_query :
        post_list = post_list.filter(
            Q(name__icontains = search_query)|
            Q(description__icontains= search_query) |
            Q(category__name__icontains= search_query)
        ).distinct()

    
    paginator = Paginator(post_list, 5) # Show 25 posts per page
    page = request.GET.get('page')
    post_list = paginator.get_page(page)

    context = {
        'post_list' : post_list,
        'post_category' :post_category,
    }

    return render(request, 'post/post_list.html', context)


def post_detail(request,slug):
    post_detail=Posts.objects.get(slug=slug)
    
    context = {
        'post' : post_detail,
    }

    return render(request, 'post/post_detail.html', context)
