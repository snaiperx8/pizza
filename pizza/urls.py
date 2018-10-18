from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static 
from django.conf import settings

from authenticate_app.views import login_view, logout_view, signup_view, home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home-url'),
    path('accounts/login/', login_view, name = 'login-url'),
    path('accounts/logout/', logout_view, name = 'logout-url'), 
    path('accounts/signup/', signup_view, name = 'signup-url'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
