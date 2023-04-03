from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404

urlpatterns = [
    path('', include('recipe.urls')),
    path('final_user/', include('final_user.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.final_user.views.handler404'

handler500 = 'apps.final_user.views.handler500'
