from django.db.models.signals import post_save
from django.shortcuts import render

from .models import Post, Category


# Create your views here.

def home_page(request):
	categories = Category.objects.all()
	posts = Post.objects.all()
	context = {'categories':categories ,'posts':posts}
	return render(request,'home.html',context)