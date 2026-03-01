from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.db.models import Q


def home_page(request):
	posts = Post.objects.all().order_by('-created_at')
	context = {
		'posts': posts[4:][:5],
		'hot_posts': posts[:4],
	}
	return render(request, "index.html", context)


def all_news_page(request):
	posts = Post.objects.all().order_by('-created_at')
	context = {
		'posts': posts
	}
	return render(request, "all-news.html", context)


def news_by_category(request, pk):
	category = get_object_or_404(Category, pk=pk)
	posts = Post.objects.filter(category=category).order_by('-created_at')
	context = {
		'category': category,
		'posts': posts
	}
	return render(request, "news-by-category.html", context)


def search_page(request):
	return render(request, "search.html")


def search_results(request):
	query = request.GET.get('q')
	results = []
	if query:
		results = Post.objects.filter(
			Q(title__icontains=query) | Q(content__icontains=query)
		)
	context = {
		'query': query,
		'results': results
	}
	return render(request, "search-results.html", context)


def read_news_page(request, pk):
	post = get_object_or_404(Post, pk=pk)
	context = {
		'post': post
	}
	return render(request, "read-news.html", context)
