""" framework"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
""" built-in """
#import datetime
#import math
""" package, modules """

from blog import settings
from posts.views import(
    main_page_view,
    posts_view,
    post_detail_view,
    post_create_view
)
from users.views import register_view, auth_view, logout_view

"""
client --> /
DJANGO: client --> includes [(admin/, admin_vew), (/, first_view)]
VIEW: client_request --> first_view(client_request)
"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('posts/', posts_view),
    path('posts/<int:id>/', post_detail_view),
    path('posts/create/', post_create_view),

    path('users/register/', register_view),
    path('users/login/', auth_view),
    path('users/logout', logout_view)


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


