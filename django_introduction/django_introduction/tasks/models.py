from django.db import models


# Maps to a database table
class Task(models.Model):
    # varchar(30) NOT NULL
    title = models.CharField(
        max_length=30,
        null=False)

    description = models.TextField()


