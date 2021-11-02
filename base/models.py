from django.db import models


class Question(models.Model):
    content = models.TextField()
    available = models.BooleanField(default=False)
    answers = models.JSONField()
    right_answer = models.IntegerField(choices=[
        (0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'),
    ])

    def __str__(self):
        return self.content
