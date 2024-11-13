from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
