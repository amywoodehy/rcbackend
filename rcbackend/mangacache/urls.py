from django.conf.urls import url
from mangacache import views

urlpatterns = [
    url(r'^catalog/$', views.catalog_list),
    url(r'^manga/(?P<manga_name>[A-Za-z]+/)$', views.manga),

]