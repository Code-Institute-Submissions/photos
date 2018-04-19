from django.db import models
from photos.models import Photo
from django.core.validators import MaxValueValidator, MinValueValidator


#Create your models here.
class Review(models.Model):
    reviewer = models.ForeignKey('auth.User', blank=False, related_name="reviews_written")   
    photo = models.ForeignKey(Photo, blank=False, related_name="reviews_received")
    content = models.CharField(max_length=254, default='')
   
    rating = models.IntegerField(blank=False, default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    
   
    
    
    
    @property
    def stars(self):
        return range(self.rating)
    
    def __str__(self):
        return self.content
        