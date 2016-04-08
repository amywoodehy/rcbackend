from django.db import models


# Create your models here.
class Author(models.Model):
    """
        Для получения манги по автору. Нужно ли?
    """
    name = models.CharField(max_length=100)
    url = models.URLField()
    image = models.ImageField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "name: {}\nurl: {}\ndescription: {}\n".format(
            self.name,
            self.url,
            self.description
        )


class Manga(models.Model):
    """
        Для католога манги. содержит ссылки на все главы манги
    """
    author = models.ForeignKey(Author, related_name='author_works')
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return "manga: {}\nurl: {}".format(self.manga_name, self.url)


class Poster(models.Model):
    manga = models.ForeignKey(Manga, related_name='posters')
    image = models.ImageField()

    def __str__(self):
        return "Poster for {}".format(self.manga.name)


class Chapter(models.Model):
    manga = models.ForeignKey(Manga, related_name='chapters')
    name = models.CharField(max_length=100, null=True)
    tom = models.IntegerField()
    number = models.IntegerField()
    added = models.DateTimeField()

    class Meta:
        ordering = ('number',)

    def __str__(self):
        return "{} chapter of {} manga".format(self.number, self.manga.name)


PageSizes = {
    "small",
    "medium",
    "big",
    "retina"
}


class Page(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='page')
    # size = models.CharField(choices=PageSizes)
    # size_x = models.IntegerField(validators=[lambda x: x > 0])
    # size_y = models.IntegerField(validators=[lambda x: x > 0])
    number = models.IntegerField()
    url = models.URLField()
    # image = models.ImageField()

    def __str__(self):
        return "{} page of {} chapter of {}".format(
            self.number, self.chapter.number, self.chapter.manga.name
        )

