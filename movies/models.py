from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):

    STATUS_CHOICES = [
        ('want', 'Хочу посмотреть'),
        ('watching', 'Смотрю'),
        ('watched', 'Посмотрел'),
    ]

    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='want'
    )
    rating = models.PositiveIntegerField(
        choices=[(i, i) for i in range(1, 11)],
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='movies'
    )

    def __str__(self):
        return self.title