from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def post_amount(self):
        return self.post_set.count()

    def __str__(self):
        return self.name
