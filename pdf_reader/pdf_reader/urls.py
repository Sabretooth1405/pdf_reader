"""pdf_reader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as users_views
from pdfs import views as pdfs_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', users_views.about, name="about"),
    path('admin/', admin.site.urls),
    path("register/", users_views.register, name="register"),
    path("login/", users_views.login, name="login"),
    path("logout/", users_views.logout, name="logout"),
    path("profile/", users_views.profile, name="profile"),
    path("upload/",pdfs_views.file_upload_view,name="upload"),
    path("user/update-user/<int:pk>",
         users_views.UpdateUserProfile.as_view(), name="update-user"),
    path("user/update-image/<int:pk>",
         users_views.UpdateProfileImg.as_view(), name="update-user-image"),
    path('users/delete/<int:pk>',
         users_views.UserDeleteView.as_view(), name='user-delete'),
    path('list', pdfs_views.TextListView.as_view(), name='text-list'),
    path("detail/<int:pk>", pdfs_views.TextDetailView.as_view(), name="text-detail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
