"""Book_review URL Configuration

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
from django.urls import path,include
from book_app import views as book_view
from django.contrib.auth import views as  auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('book_app.urls')),
    path("Author/profile/",  book_view.Author_profile, name= 'profile'),
    path("Reader/profile/", book_view.Reader_profile, name='Reader_profile'),
    path("Author/signup/", book_view.register, name='register'),
    path("Reader/signup/", book_view.Reader_register, name='Reader_register'),
    path('Author/login/', book_view.Author_login, name='login'),
    path('Reader/login/', book_view.Reader_login, name='Reader_login'),
    path('Author/UpdateProfile/', book_view.Author_upprofileup, name='author_update_profile'),
    path('Reader/UpdateProfile/', book_view.Reader_upprofileup, name='reader_update_profile'),
    path("Author/logout/", auth_views.LogoutView.as_view(template_name='book_app/Reader/logout.html'), name='Author_logout'),
    path("Reader/logout/", auth_views.LogoutView.as_view(template_name='book_app/Reader/logout.html'),
                       name='Reader_logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
