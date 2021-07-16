from django.db import models

# Create your models here.
class Post(models.Model):
    title=models. CharField('post title', max_length=50)
    body=models. TextField('Text body')


    def __str___(self):
        return self.title