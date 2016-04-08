from datetime import datetime

from rest_framework import serializers
from mangacache.models import Chapter, Manga, Author, Poster, Page


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    url = serializers.URLField()

    description = serializers.CharField(max_length=1000)

    class Meta:
        model = Author


class ChapterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    tom = serializers.IntegerField(required=False)
    number = serializers.IntegerField(required=True)
    added = serializers.DateTimeField()

    class Meta:
        model = Chapter

    def create(self, validated_data):
        return Chapter.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.tom = validated_data.get('tom', instance.tom)
        instance.number = validated_data.get('number', instance.number)
        instance.added = validated_data.get('added', instance.added)


class MangaSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    url = serializers.URLField()
    # posters = serializers.PrimaryKeyRelatedField(many=True, queryset=Poster.objects.all())
    chapters = ChapterSerializer(many=True)
    # chapters = serializers.PrimaryKeyRelatedField(many=True, queryset=Chapter.objects.all())

    def create(self, validated_data):
        manga = Manga.objects.create(name=validated_data['name'],
                             url=validated_data['url'])
        for item in validated_data['chapters']:
            chapter = Chapter.objects.create(
                name=item.get("name", ""),
                tom=item.get("tom", 0),
                number=item.get("number", 0),
                added=item.get("added", datetime.now()),
                manga=manga
            )
            chapter.save()
        return manga


