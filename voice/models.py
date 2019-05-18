from django.db import models
import uuid
# Create your models here.

class Muscle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    newsText = models.TextField()
    newsVoice = models.FileField()
    textType = models.CharField(max_length=30)
