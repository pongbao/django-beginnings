"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# added modules
# referencing other URLconfs
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

    # added paths
    # path(route, view, [kwargs, name])
    # route: string that contains a URL pattern; when processing a request, Django starts at the first pattern in urlpatterns and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches; patterns don’t search GET and POST parameters, or the domain name
    # view: alls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments
    path('polls/', include('polls.urls')),
    
]
