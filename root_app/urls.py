from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
