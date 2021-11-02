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


class Participant(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Answer(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['participant', 'question'], name='unique_answer')
        ]
