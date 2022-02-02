from django.urls import include, path
from . import views

urlpatterns = [
    path(r'^admin/',admin.site.urls),
    path('account/', include('account.urls')),
]