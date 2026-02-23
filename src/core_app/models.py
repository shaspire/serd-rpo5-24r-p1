from django.db import models


class Category(models.Model):
	name = models.CharField('Category Name', max_length=100)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField( 'Title', max_length=255)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
	image_url = models.CharField('Image URL', max_length=500)
	content = models.TextField('Description')
	created_at = models.DateTimeField('Publication Datetime', auto_now_add=True)

	def __str__(self):
		return self.title