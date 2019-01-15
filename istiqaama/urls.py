from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
# from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('dashboard.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    # url(r'^pdf/$', views.generate_view, name = 'generate_view'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
