from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    def __Str__(self):
        return self.name