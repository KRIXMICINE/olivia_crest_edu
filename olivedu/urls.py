from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact.html', views.contact, name="contact" ),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('team/', include('team.urls')),
    path('faq/', include('faq.urls')),
    path('privacy.html', views.privacy, name="privacy" ),
    path('terms.html', views.terms, name="terms" ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)