from django.db import models

class todo(models.Model):
        work_id = models.AutoField(primary_key=True)
        work =models.CharField(max_length=50)
        due_date = models.DateField()
        desc = models.CharField(max_length=1000,  default="")
