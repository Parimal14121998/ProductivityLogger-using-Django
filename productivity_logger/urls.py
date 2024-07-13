from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('allauth.urls')),
    path('', RedirectView.as_view(url='/accounts/login/', permanent=True)),
]
