from django.db import models

# Create your models here.
class library_item(models.Model):
    library_Id = models.IntegerField(primary_key=True)
    title=models.CharField(max_length=255)
    copies=models.IntegerField()
    pub_name=models.ForeignKey('Publisher', on_delete=models.PROTECT)
    Image=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title

class magazine(models.Model):
    Mag_ID = models.OneToOneField('library_item', on_delete=models.CASCADE, primary_key = True)
    publish_date = models.DateField()
    mag_type = models.CharField(max_length=255)

class journal(models.Model):
    Jour_ID = models.OneToOneField('library_item', on_delete=models.CASCADE, primary_key = True)
    volume = models.IntegerField()
    journal_number = models.IntegerField()

class book_collection(models.Model):
    Book_ID = models.OneToOneField('library_item', on_delete=models.CASCADE, primary_key = True)
    edition = models.IntegerField()
    book_type = models.CharField(max_length=255)

class author(models.Model):
    Book_Aur_ID = models.ForeignKey('library_item', on_delete=models.CASCADE, primary_key = True)
    A_name = models.CharField(max_length=255)
    class Meta:
        unique_together = ('Book_Aur_ID','A_name')

class Publisher(models.Model):
    name = models.CharField(max_length=255,primary_key=True)
    url = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Borrower(models.Model):
        borrower_Id = models.IntegerField(primary_key=True)
        name=models.CharField(max_length=255)
        email = models.EmailField(max_length=254)
        blacklisted=models.BooleanField()
        academics=models.BooleanField()
        fine=models.IntegerField()
        b_rank=models.CharField(max_length=255)

class Borrows(models.Model):
    Borrows_ID = models.OneToOneField('library_item', on_delete=models.CASCADE, primary_key = True)
    BID = models.ForeignKey('Borrower', on_delete=models.CASCADE)
    returndate= models.DateField()
    checkoutdate= models.DateField()

    class Meta:
        unique_together = ('Borrows_ID','BID')
