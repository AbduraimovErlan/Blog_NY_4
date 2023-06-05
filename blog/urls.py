"""
URL configuration for blog project.

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
from posts.views import first_view
from posts.views import redirect_to_youtube_view


"""
client --> /
DJANGO: client --> includes [(admin/, admin_vew), (/, first_view)]
VIEW: client_request --> first_view(client_request)
"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first_view),
    path('youtube/', redirect_to_youtube_view)
]
