from django.db import models

import uuid

# class Messages(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     body = models.TextField(max_length=500)
#     creation_date = models.DateTimeField(auto_now_add=True)

# class My_messages(models.Model):
#     id = models.UUIDField(primary_key=True, default=str(uuid.uuid4)[:8], editable=False)
#     body = models.TextField(max_length=500)
#     creation_date = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.body

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)
    year = models.IntegerField()
    
    class Meta:
        ordering = ('title',)

def resolveMovies():
    pass

string = 'This is a string'
another = "God's plan!"
        