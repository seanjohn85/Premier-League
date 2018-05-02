"""epl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #home directory routing
    url(r'^$', include('mmsca2.urls')),
    url(r'^requets/', include('requets.urls')),
    url(r'^footballdata/', include('footballdata.urls')),
    url(r'^rest/', include('rest.urls')),
    url(r'^mmsca2/', include('mmsca2.urls')),
    url(r'^mmsca2/', include('mmsca2.urls')),
    url(r'^api/mmsca2/', include('mmsca2.api.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
