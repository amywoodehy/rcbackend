from datetime import datetime

from rest_framework import serializers

from mangacache.models import Chapter, Manga, Author


class MangaDetailSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    url = serializers.URLField()
    description = serializers.CharField(max_length=65525)

    def create(self, validated_data):
        return Manga.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.description = validated_data.get("description", instance.description)
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    url = serializers.URLField()
    description = serializers.CharField(max_length=1000)
    manga = MangaDetailSerializer(many=True)

    class Meta:
        model = Author

    def create(self, validated_data):
        author = Author.objects.create(
            name=validated_data["name"],
            url=validated_data["url"],
            description=validated_data["description"]
        )
        for item in validated_data["manga"]:
            item["author"] = author
            self.manga.create(**item)
            self.manga.save()
        return author


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter

    def create(self, validated_data):
        chapter = Chapter.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.tom = validated_data.get('tom', instance.tom)
        instance.number = validated_data.get('number', instance.number)
        instance.added = validated_data.get('added', instance.added)
        for item in validated_data["pages"]:
            page = instance.pages.update(**item)
            page.save()
        return instance


class MangaSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    chapters = ChapterSerializer(many=True)

    def create(self, validated_data):
        manga = Manga.objects.get_or_create(name=validated_data["name"])
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
