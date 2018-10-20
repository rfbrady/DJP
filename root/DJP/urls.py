"""DJP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path

# a note on path. It is passed route, view, kwargs and name
# route is the url pattern
# once django finds a pattern, it calls the specified view Function
# arbitrary keyword args can be passed in a dict to a view
# naming a URL allows you to refer to it unambiguously elsewhere
urlpatterns = [
    path('admin/', admin.site.urls),
    #include means that anything that leads up to blog will be ignored
    path('blog/', include('blog.urls'))
]
