from django.shortcuts import render, get_object_or_404
from .models import post
from category.models import category
from taggit.models import Tag 
from team.models import Team
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.db.models import Q


# Create your views here.
def blog(request, category_slug=None):
    categories = None
    Posts = None        
        
    if category_slug != None:
        categories = get_object_or_404(category, slug = category_slug)
        Posts = post.objects.filter(category=categories)
        post_count = Posts.count()
    else:        
        Posts = post.objects.all()
        post_count = Posts.count()
        category_count = category.objects.annotate(post_count=Count('post'))
        
        
    # Setting up the pagination.    
    category_count = None
    items_per_page = 4
    query = request.GET.get('q')
    
    if query is not None:
        Posts = post.objects.filter(Q(title__icontains=query))
    
    paginator = Paginator(Posts, items_per_page )
    page = request.GET.get('page')
    try:
        Posts = paginator.get_page(page)
    except PageNotAnInteger:
        Posts = paginator.page(1)
    except EmptyPage:
        Posts = paginator.get_page(paginator.num_pages)
    
            
    context = {'categories': categories, 'Posts': Posts, 'post_count': post_count, 'category_count': category_count}
    return render(request, 'blog.html', context)




def blog_details(request, category_slug, post_slug, tag_slug=None):
    tag = None
    related_posts = None
    Posts = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        single_post = post.filter(tags__in=[tag])
        related_posts = post.objects.filter(tags__in=[tag]).exclude(slug=post_slug)
    try:
        single_post = post.objects.get(category__slug=category_slug, slug=post_slug)
        Posts = post.objects.order_by('-publish')[:3]
    except Exception as e:
        raise e
    
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     Posts = post.objects.filter(title__icontains=q)
    # else:
    #     Posts = post.objects.all()
            
    context = {'single_post': single_post, 'tag': tag, 'related_posts': related_posts, 'Posts':Posts}
    return render(request, 'blog_details.html', context)

