from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Variant(models.Model):
    OPTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='variants')
    option = models.CharField(max_length=1, choices=OPTION_CHOICES)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['question'],
                condition=models.Q(is_correct=True),
                name='unique_correct_variant_per_question'
            )
        ]

    def __str__(self):
        return f"{self.option}: {self.text} ({'Correct' if self.is_correct else 'Wrong'})"
