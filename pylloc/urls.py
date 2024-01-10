from django.contrib import admin
from django.urls import path
from users.views import allocate_seq

urlpatterns = [
    path('admin/', admin.site.urls),
    path('allocate-seq/', allocate_seq, name='allocate_seq'),
]
