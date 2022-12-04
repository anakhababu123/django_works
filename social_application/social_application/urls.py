"""social_application URL Configuration

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
from django.urls import path
from django.views import View
from social import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path("register",views.SignUpView.as_view(),name="register"),
    path("login",views.LoginView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="home"),
    path('questions/<int:id>/comments/add',views.add_answer,name="add-comment"),
    path("post/<int:id>like/",views.upvote_view,name="like"),
    path("signout",views.sign_out,name="signout"),
    path("post/all",views.MyQuestionsView.as_view(),name="posts")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


