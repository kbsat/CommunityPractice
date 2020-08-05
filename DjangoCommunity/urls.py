from django.contrib import admin
from django.urls import path
import community.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', community.views.main, name="main"),
    path('post/', community.views.post, name="post"),
    path('new/', community.views.new, name="new"),
    path('detail/<int:post_id>', community.views.detail, name="detail"),
    path('delete/<int:post_id>', community.views.delete, name="delete"),
    path('update/<int:post_id>', community.views.update, name="update"),
    path('update_save/<int:post_id>',
         community.views.update_save, name="update_save"),
]
