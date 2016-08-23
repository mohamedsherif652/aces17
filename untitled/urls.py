
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^aces/', include('ACES.urls')),
    url(r'^',include('ACES.urls'))
]
