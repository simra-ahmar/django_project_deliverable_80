from django.db import models


# Create your models here.

class Post(models.Model):
	Name= models.CharField(max_length=100)
	Location=models.TextField()
	#Cuisines=models.TextField()
	#PriceRange=models.TextField()
	#Ratings=models.TextField()
	
class Post1(models.Model):
	Name= models.CharField(max_length=100)
	Location=models.CharField(max_length=100)
	Cuisines=models.CharField(max_length=100)
	PriceRange=models.IntegerField()
	Ratings=models.CharField(max_length=100)

	def __str__(self):
		return self.Name 
class Dish(models.Model):
	
	name=models.CharField(max_length=100)
	highest_price=models.IntegerField()

	def __str__(self):
		return self.name
class Menu1(models.Model):
	
	name=models.CharField(max_length=100)
	price=models.IntegerField()
	restaurant=models.ForeignKey(Post1, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
class Menu2(models.Model):
	
	name=models.CharField(max_length=100)
	price=models.IntegerField()
	restaurant=models.CharField(max_length=100)

	def __str__(self):
		return self.name
