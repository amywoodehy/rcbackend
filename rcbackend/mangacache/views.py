from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from mangacache.models import MangaCatalog, MangaChapter
from mangacache.serializers import MangaChapterSerializer, MangaCatalogSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def catalog_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        chapter = MangaCatalog.objects.all()
        serializer = MangaCatalogSerializer(chapter, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MangaCatalogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def manga(request, manga_name):

    try:
        catalog = MangaCatalog.objects.get(manga_name=manga_name)
    except MangaCatalog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MangaCatalogSerializer(catalog)
        return JSONResponse(serializer.data)
