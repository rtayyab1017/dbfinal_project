from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class library_item(models.Model):
    library_Id = models.IntegerField(primary_key=True)
    title=models.CharField(max_length=255)
    copies=models.IntegerField()
    pub_name=models.ForeignKey('Publisher', on_delete=models.PROTECT)
    Image=models.ImageField(upload_to='images/')
    pdf = models.FileField(upload_to='pdf/', default = 'string')
    def __str__(self):
        return self.title

class magazine(models.Model):
    magazine_Id = models.OneToOneField('library_item', on_delete=models.CASCADE, primary_key = True)
    publish_date = models.DateField()
    mag_type = models.CharField(max_length=255)

class journal(models.Model):
    journal_Id = models.OneToOneField('library_item', on_delete=models.CASCADE, primary_key = True)
    volume = models.IntegerField()
    journal_number = models.IntegerField()

class book_collection(models.Model):
    book_Id = models.OneToOneField('library_item', on_delete=models.CASCADE, primary_key = True)
    edition = models.IntegerField()
    book_type = models.CharField(max_length=255)

class author(models.Model):
    Book_Aur_ID = models.OneToOneField('library_item', on_delete=models.CASCADE, primary_key = True)
    A_name = models.CharField(max_length=255)
    class Meta:
        unique_together = ('Book_Aur_ID','A_name')

class Publisher(models.Model):
    name = models.CharField(max_length=255,primary_key=True)
    url = models.CharField(max_length=255)
    def __str__(self):
        return self.name

def return_date_time():
    now = timezone.now()
    return now + timedelta(days=120)


class PersonExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key='True')
    blacklisted=models.BooleanField(default='False')
    fine=models.IntegerField(null='True')
    checkoutdate = models.DateField(default=timezone.now)
    returndate = models.DateField(default=return_date_time)
