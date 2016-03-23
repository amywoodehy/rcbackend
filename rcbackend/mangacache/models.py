from django.db import models


# Create your models here.
class MangaAuthor(models.Model):
    """
        Для получения манги по автору. Нужно ли?
    """
    name = models.CharField(max_length=100)
    url = models.URLField()
    image = models.ImageField()
    description = models.CharField(max_length=1000)


class MangaCatalog(models.Model):
    """
        Для католога манги. содержит ссылки на все главы манги
    """
    author = models.ForeignKey(MangaAuthor, related_name='author_works')
    manga_name = models.CharField(max_length=30)
    url = models.URLField()
    poster = models.ImageField()


class MangaPoster(models.Model):
    catalog = models.ForeignKey(MangaCatalog, related_name='posters')
    image = models.ImageField()


class MangaChapter(models.Model):
    catalog = models.ForeignKey(MangaCatalog, related_name='chapters')
    chapter_name = models.CharField(max_length=100, null=True)
    tom = models.IntegerField()
    chapter = models.IntegerField()
    added = models.DateField()

    class Meta:
        unique_together = ('catalog', 'chapter')
        ordering = ('chapter',)


class MangaPage(models.Model):
    chapter = models.ForeignKey(MangaChapter, related_name='page')
    url = models.URLField()
    image = models.ImageField()

