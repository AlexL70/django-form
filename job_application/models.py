from django.db import models


class JobAppForm(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    start_date = models.DateField()
    occupation = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}> ({self.occupation}) ready to start at {self.start_date}"
