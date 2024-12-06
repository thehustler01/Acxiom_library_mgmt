from django.urls import path
from .views import home_view,custom_login_view, user_home, admin_home,log_out

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', custom_login_view, name='login'),
    path('user_home/', user_home, name='user_home'),
    path('admin_home/', admin_home, name='admin_home'),
    path('logout/', log_out, name='logout'),
]