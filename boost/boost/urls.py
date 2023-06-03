"""
URL configuration for boost project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from app import views
from app.ajax_queryes import ajax_notes

from boost import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.sign_up, name='sign_up'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    path('profile/', views.profile, name='profile'),
    path('document<int:pk>', views.doc_page, name='doc_page'),
    path('document<int:pk>/edit', views.doc_page_edit, name='doc_page'),
    path('create/', views.create_docs, name='create_docs'),

    path('document<int:pk>/getdata', ajax_notes.get_data, name='data_get_ajax'),
    path('documents/postlikedata', ajax_notes.like_post, name='like_post_ajax'),
    path('documents/postdislikedata', ajax_notes.dislike_post, name='dislike_post_ajax'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
