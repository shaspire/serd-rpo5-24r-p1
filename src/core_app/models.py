from django.db import models


class Category(models.Model):
    name = models.CharField('Category Name', max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField( 'Title', max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    image = models.FileField(upload_to="posts/")
    content = models.TextField('Description')
    created_at = models.DateTimeField('Publication Datetime', auto_now_add=True)

    def __str__(self):
        return self.title

class Advertisement(models.Model):
    name = models.CharField("Company name", max_length=255, default="Company name")
    image = models.FileField(upload_to="ads/")

    def __str__(self):
        return self.name