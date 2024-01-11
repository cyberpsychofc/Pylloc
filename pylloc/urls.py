from django.contrib import admin
from django.urls import path
from users.views import allocate_seq, preference

urlpatterns = [
    path('admin/', admin.site.urls),
    path('allocate-seq/', allocate_seq, name='allocate_seq'),
    path('<int:user_pk>/preference/',preference, name='preference'),
]
