from django.db import models


class Project(models.Model):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    name = models.CharField(max_length=260, default='')
    description = models.TextField(default='')
    date = models.DateTimeField()
    icon = models.CharField(max_length=260, default='')
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default=LOW,
    )

    def __str__(self):
        return self.name
