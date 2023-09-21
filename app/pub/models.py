from django.db import models

from user.models import User


class AbstractPost(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Forum(AbstractPost):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(AbstractPost):
    text = models.CharField(max_length=255)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
