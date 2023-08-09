from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('polls.urls')),
    path('adminSide/', include('admin_side.urls')),
    path('admin/', admin.site.urls),
    path('Nutritionist/', include('Nutritionist_side.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)