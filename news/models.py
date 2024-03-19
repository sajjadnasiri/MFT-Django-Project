from django.db import models
from django.contrib.auth.models import User

# Casreat your models here.
class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news')
    # tag
    # category = models.CharField(max_length=256)
    active = models.BooleanField(default=False)
    ceated_date = models.DateTimeField(auto_now_add=True)

    def abstract(self):
        return self.content[:60] + " ..."
    
    def __str__(self):
        return self.title