from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	address=models.TextField()
	gender=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	cpassword=models.CharField(max_length=100)
	image=models.ImageField(upload_to="images/",default="",blank=True,null=True)
	status=models.CharField(max_length=100, default="inactive")
	usertype=models.CharField(max_length=100,default="user")

	def __str__(self):
		return self.firstname+"-"+self.lastname

class Area(models.Model):
	CHOICES=(
		('Sg highway,Ahmedabad West','Sg highway,Ahmedabad West'),
		('Shela,Ahmedabad West','Shela,Ahmedabad West'),
		('South Bopal,Ahmedabad West','South Bopal,Ahmedabad West'),
		('Chandkhelda,Ahmedabad North','Chandkhelda,Ahmedabad North'),
		('Naroda,Ahmedabad East','Naroda,Ahmedabad East'),
		('Bopal,Ahmedabad West','Bopal,Ahmedabad West'),
		('Thaltej,Ahmedabad West','Thaltej,Ahmedabad West'),
		('Satellite,Ahmedabad West','Satellite,Ahmedabad West'),
		('Gota,Ahmedabad North','Gota,Ahmedabad North'),
	)
	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	Area=models.CharField(max_length=100,choices=CHOICES)
	Looking_To=models.CharField(max_length=100)
	Property_Kind=models.CharField(max_length=100)
	Address=models.TextField()
	Property_Layout=models.TextField()
	Property_Ownership=models.CharField(max_length=100)
	Super_Area=models.TextField()
	facing_road=models.TextField()
	Property_Flooring=models.CharField(max_length=100)
	Water_source=models.CharField(max_length=100)
	Furnishing=models.CharField(max_length=100)
	Facing=models.CharField(max_length=100)
	Property_id=models.TextField()
	Price=models.IntegerField()
	Additional_Details=models.TextField()
	Contact=models.IntegerField()
	Image1=models.ImageField(upload_to='Property_Images/', default="" ,null="",blank=True)
	Image2=models.ImageField(upload_to='Property_Images/', default="" ,null="",blank=True)
	Image3=models.ImageField(upload_to='Property_Images/', default="" ,null="",blank=True)
	Image4=models.ImageField(upload_to='Property_Images/', default="" ,null="",blank=True)
	Image5=models.ImageField(upload_to='Property_Images/', default="" ,null="",blank=True)
	
	def __str__(self):
		return self.Area+" - "+self.Address

class Wishlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	area=models.ForeignKey(Area,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.area.Area+"  - "+self.area.Address

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	area=models.ForeignKey(Area,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)
	Price=models.IntegerField()
	total_price=models.IntegerField()
	

	def __str__(self):
		return self.Area+"  - "+self.Address