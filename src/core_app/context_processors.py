from core_app.models import Category, Advertisement
from django.core.handlers.wsgi import WSGIRequest
from random import sample

def categories(request: WSGIRequest):
	return {'categories': Category.objects.all()}

def advertisements(request: WSGIRequest):
	ads = Advertisement.objects.all()
	if len(ads) > 2:
		ads = sample(list(ads),2)
	return {'ads': ads}