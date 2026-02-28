from core_app.models import Category, Advertisement
from django.core.handlers.wsgi import WSGIRequest
from random import sample

def categories(request: WSGIRequest):
	return {'categories': Category.objects.all()}

def advertisements(request: WSGIRequest):
	return {'ads': sample(list(Advertisement.objects.all()),2)}