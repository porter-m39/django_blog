from django.db import models
from PIL import Image
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    slug = models.SlugField(null=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts",blank=True)
    #images = models.ManyToManyField("Image",blank=True)
    banner = models.ImageField(default="default.png", blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})
    
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.author} on '{self.post}'"
    

# class Image(models.Model):
#     uploads = models.ImageField(blank=True)
#     #parent_post = models.ForeignKey(Post,on_delete=models.CASCADE)
