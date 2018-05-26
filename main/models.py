import json
from django.db import models
from django.utils import timezone

# Create your models here.
class ScrapyItems(models.Model):
    unique_id = models.CharField(max_length=100, blank=True)
    data = models.TextField()
    date = models.DateField(default=timezone.now)

    @property
    def to_dict(self):
        data = {
            'data': json.loads(self.data),
            'date': self.date
        }
        return data

    def __str__(self):
        return self.unique_id