from django.db import models

class Day(models.model):
    date = models.DateField(auto_now=True)

    notes = models.TextField()

    above_treeline = models.IntField()
    near_treeline = models.IntField()
    below_treeline = models.IntField()
