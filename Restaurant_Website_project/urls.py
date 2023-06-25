"""
URL configuration for Restaurant_Website_project project.

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
from django.contrib import admin
from django.urls import path
from Hero_page.views import homePageview, aboutPage, menuPage, blogPage, contactPage, elementPage, singleBlogPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePageview, name = 'home'),
    path('about/', aboutPage, name = 'about'),
    path('menu/', menuPage, name = 'menu'),
    path('blog/', blogPage, name = 'blog'),
    path('single_blog/', singleBlogPage, name = 'singleBlog'),
    path('contact/', contactPage, name = 'contact'),
    path('elements/', elementPage, name = 'element'),
]
