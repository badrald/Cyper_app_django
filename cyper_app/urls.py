from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# viwes الخاص بإستدعاء كل فنشن من  URL الروابط التي تظهر في
urlpatterns = [
    path("", views.index, name="index"),
    path("xss/", views.xss_vulnerable, name="xss"),
    path("sql/", views.sql_injection, name="sql"),
    path("csrf/", views.csrf_vulnerable, name="csrf"),
    path("dos/", views.dos_vulnerable, name="dos"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
