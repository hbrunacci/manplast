"""manplast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

from django.contrib.auth import views as auth_views
from materiales.views import MarcoCRUD, MaterialCRUD
from clientes.views import ClienteCRUD
from piezas.views import PiezaCRUD
from .views import IndexView

marcoCRUD = MarcoCRUD()
materialCRUD = MaterialCRUD()
clienteCRUD = ClienteCRUD()
piezaCRUD = PiezaCRUD()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url(r'', include(marcoCRUD.get_urls())),
    url(r'', include(materialCRUD.get_urls())),
    url(r'', include(clienteCRUD.get_urls())),
    url(r'', include(piezaCRUD.get_urls())),
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

