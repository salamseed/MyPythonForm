from django.db import models

class DailyTask(models.Model):
    task=models.CharField(max_length=250)
    priority=models.IntegerField()
    date=models.DateField()
    def __str__(self):
       return self.task
