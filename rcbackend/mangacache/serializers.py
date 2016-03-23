from rest_framework import serializers
from mangacache.models import MangaChapter, MangaCatalog, MangaAuthor


class MangaChapterSerializer(serializers.ModelSerializer):
    pages = serializers.StringRelatedField(many=True)

    class Meta:
        model = MangaChapter
        fields = ('manga_name', 'chapter_name', 'tom', 'chapter', 'pages')


class MangaCatalogSerializer(serializers.ModelSerializer):
    chapters = serializers.StringRelatedField(many=True)

    class Meta:
        model = MangaCatalog
        fields = ('manga_name', 'chapters')