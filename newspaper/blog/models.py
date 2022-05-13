from django.db import models

 

class Post(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.title




class News(models.Model):
    title = models.CharField(max_length=400)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()


    def __srt__(self):
        return self.title