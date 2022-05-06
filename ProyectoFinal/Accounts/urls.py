from django.urls import path
from .views import signup, login, log_out

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', log_out, name='logout'),
]