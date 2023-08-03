from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
# from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog.urls')),
    # url(r'^admin/', admin.site.urls),
    # url(r'', include('blog.urls')),
]
