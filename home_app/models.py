from django.db import models
from django.core.validators import MaxValueValidator

class EnergyValue(models.Model):

	name = models.CharField(max_length = 30)
	protein = models.IntegerField(validators = [MaxValueValidator(100)])
	fat = models.IntegerField(validators = [MaxValueValidator(100)])
	carbohydrate = models.IntegerField(validators = [MaxValueValidator(100)])
	ccal = models.IntegerField(validators = [MaxValueValidator(5000)])

	def __str__(self):
		return self.name

class Pizza(models.Model):
	photo = models.ImageField(upload_to = 'upload_photos/pizza_photo',
							 default = 'media/photos_def/pizza/pizza_def.jpg', blank = False)
	name = models.CharField(max_length = 30)
	ingredients = models.TextField()
	cost = models.IntegerField(blank = False)
	energ_val = models.ForeignKey(EnergyValue, on_delete = models.DO_NOTHING)

	def __str__(self):
		return self.name
# Create your models here.
