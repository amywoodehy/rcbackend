from django.shortcuts import get_object_or_404

from mangacache.models import Chapter, Page, Manga, Author
from mangacache.serializers import AuthorSerializer, MangaSerializer, ChapterSerializer
from rest_framework import generics, permissions
from mangacache.serializers import AuthorSerializer, MangaSerializer, ChapterSerializer


class MangaList(generics.ListCreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MangaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    lookup_field = 'name'


class ChapterList(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def perform_create(self, serializer):
        serializer.save()


class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {
            'name': self.kwargs['name'],
            'number': self.kwargs['number']
            }
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

