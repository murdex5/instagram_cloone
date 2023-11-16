from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# def get_default_user_id():
#     return User.objects.first()
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ResizedImageField(size=[1000, 1000], upload_to="uploads/", null=True, blank=True)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.title



# class Post(models.Model):
#     post_id = models.AutoField(primary_key=True)
#     post_author = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user_id)
    
#     ## Post content
#     post_title = models.CharField(max_length=1000)
#     post_created = models.DateField(auto_now_add=True)
#     post_updated = models.DateField(auto_now=True)
#     # post_likes
#     # post_comment
#     post_image = models.ImageField(upload_to="uploads/", null=True, blank=True)
   
#     def __str__(self):
#         return self.post_title