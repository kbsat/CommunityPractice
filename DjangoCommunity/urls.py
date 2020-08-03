from django.contrib import admin
from django.urls import path
import community.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', community.views.main, name="main"),
    path('post/', community.views.post, name="post"),
    path('new/', community.views.new, name="new"),
]
