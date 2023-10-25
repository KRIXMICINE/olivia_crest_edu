from . import views
from django.urls import path



#create path here.
urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:category_slug>/', views.blog, name = 'post_by_category' ),
    path('<slug:category_slug>/<slug:post_slug>/', views.blog_details, name ='blog_details'),
    # path('author/<int:pk>/', views.author_single, name='author_single'),
    
]


# if query is not None:
#         Posts = post.objects.filter(Q(title__icontains=query))
#     else:
#         Posts = post.objects.all()