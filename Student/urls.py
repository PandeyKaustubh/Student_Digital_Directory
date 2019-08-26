from django.contrib import admin
from django.conf.urls import url , include
from Directory import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^superuser/', include('Directory.urls'))
    ]