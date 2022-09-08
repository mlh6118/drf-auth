from django.contrib.auth import get_user_model
from django.db import models


class Book(models.Model):
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                 null=True)
    book_name = models.CharField(max_length=64)
    book_author = models.CharField(max_length=32)
    review = models.TextField(default="")
    stars = models.SmallIntegerField(default="0")

    def __str__(self):
        return self.book_name
