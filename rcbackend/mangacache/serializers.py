from rest_framework import serializers
from mangacache.models import Chapter, Manga, Author, Poster, Page


class AuthorSerializer(serializers.ListSerializer):
    manga = serializers.PrimaryKeyRelatedField(many=True, queryset=Manga.objects.all())

    class Meta:
        model = Author
        fields = ('id', 'author', 'manga')


class MangaSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    url = serializers.URLField()
    posters = serializers.PrimaryKeyRelatedField(many=True, queryset=Poster.objects.all())
    chapters = serializers.PrimaryKeyRelatedField(many=True, queryset=Chapter.objects.all())


class ChapterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    tom = serializers.IntegerField(required=False)
    number = serializers.IntegerField(required=True)
    added = serializers.DateTimeField()

    pages = serializers.PrimaryKeyRelatedField(many=True, queryset=Page.objects.all())

    class Meta:
        model = Chapter

    def create(self, validated_data):
        return Chapter.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.tom = validated_data.get('tom', instance.tom)        
        instance.number = validated_data.get('number', instance.number)
        instance.added = validated_data.get('added', instance.added)
