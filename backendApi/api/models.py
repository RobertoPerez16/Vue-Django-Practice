from django.db import models

# Create your models here.

class ToDo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)+'-'+ self.title