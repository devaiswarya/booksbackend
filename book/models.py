from django.db import models

# Create your models here.
class Books(models.Model):
    Book_name=models.CharField(max_length=100)
    Book_author=models.CharField(max_length=100)
    Book_journal=models.CharField(max_length=100)
    Book_price=models.IntegerField()
    Book_description=models.CharField(max_length=100)
    Book_rating=models.IntegerField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.Book_name
    
