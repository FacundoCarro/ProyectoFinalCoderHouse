from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from .views import InicioView, PostView
from django.urls import path

urlpatterns=[
    path('',InicioView.as_view(), name='Inicio'),
    path('blog/<pk>/<slug:slug>', PostView.as_view(), name='Post'),
    path('accounts/', include(('Accounts.urls', 'accounts'), namespace='Accounts')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)