from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # TODO: for the next project, please write the variable names in English
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    terminee = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
