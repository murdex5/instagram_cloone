from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.first().id)
    
    ## Post content
    post_title = models.CharField(max_length=1000)
    post_created = models.DateField(auto_now_add=True)
    post_updated = models.DateField(auto_now=True)
    # post_image = models.ImageField(upload_to="uploads/")
   
    def __str__(self):
        return self.post_title