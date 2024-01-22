from django.contrib import admin
from django.urls import path
from users.views import allocate_seq, preference, allocate_apc
from dashboard.views import dashboard, SignUp,rms_dash

urlpatterns = [
    path('admin/', admin.site.urls),
    path('allocate-seq/', allocate_seq, name='allocate_seq'),
    path('allocate-apc/', allocate_apc, name='allocate_apc'),
    path('<int:user_pk>/preference/',preference, name='preference'),
    path('dashboard/',dashboard,name='dashboard'),
    path('signup/', SignUp ,name='SignUp'),
    path('rms/',rms_dash,name='rms_dash')
]
