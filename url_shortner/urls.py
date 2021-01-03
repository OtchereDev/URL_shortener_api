
from django.contrib import admin
from django.urls import path,include,re_path
from .views import redirector,home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/', include('api.urls')),
    # re_path(r'^[A-Za-z]{1,10}/$', redirector),
    path('<str:pk>/', redirector),

]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)