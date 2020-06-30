from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    semester = models.CharField(max_length=255)
    image =models.ImageField(upload_to='images/')


    def date_pretty(self):
        return self.date.strftime('%b %e %Y')
