from django.shortcuts import render

# Create your views here.

def homePageview(request):
    return render(request, 'Hero_page/index.html')

def aboutPage(request):
    return render(request, 'Hero_page/about.html')

def menuPage(request):
    return render(request, 'Hero_page/food_menu.html')

def contactPage(request):
    return render(request, 'Hero_page/contact.html')

def blogPage(request):
    return render(request, 'Hero_page/blog.html')

def singleBlogPage(request):
    return render(request, 'Hero_page/single-blog.html')

def elementPage(request):
    return render(request, 'Hero_page/elements.html')


