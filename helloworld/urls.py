from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
	# URL padrão
    path('', include('website.urls', namespace='website')),

    # Interface administrativa
    path('admin/', admin.site.urls),
]
