from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from mangacache import views

urlpatterns = [
    url(r'^authors/$', views.AuthorList.as_view()),
    url(r'^author/(?P<name>[A-Za-z0-9\s]+)/$', views.AuthorDetail.as_view()),
    url(r'^catalog/$', views.MangaList.as_view()),
    url(r'^manga/(?P<name>[A-Za-z0-9]+)/$', views.MangaDetail.as_view()),
    url(r'^manga/(?P<name>[A-Za-z0-9]+)/(?P<number>[0-9])/$', views.ChapterDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
