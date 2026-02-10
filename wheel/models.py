from django.db import models

class Option(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=10, default='html')

    def __str__(self):
        return self.text


class SpinHistory(models.Model):
    options_snapshot = models.TextField()  # текст всех вариантов на момент спина
    result = models.CharField(max_length=255)  # текст результата
    created_at = models.DateTimeField(auto_now_add=True)



# Create your models here.
