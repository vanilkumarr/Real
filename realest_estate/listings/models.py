from django.db import models
from django.utils.timezone import now
# Create your models here.
from realtors.models import Realtors

class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE="for Sale"
        FOR_RENT="for Rent"
    class HouseType(models.TextChoices):
        House="House"
        Condo="condo"
        Townhouse="townhouse"
        RV="RV"
    
    realtor=models.ForeignKey(Realtors,on_delete=models.DO_NOTHING)
    slug=models.CharField(max_length=200,unique=True)
    title=models.CharField(max_length=250,unique=True)
    address=models.CharField(max_length=250)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    sale_type=models.CharField(max_length=100,choices=SaleType.choices,default=SaleType.FOR_SALE)
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.DecimalField(max_digits=2,decimal_places=1)
    house_type=models.CharField(max_length=100,choices=HouseType.choices,default=HouseType.House)
    sqft=models.IntegerField()
    open_house=models.BooleanField(default=False)
    photo_main=models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_0=models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_1=models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_2=models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_3=models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_4=models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_5=models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_6=models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_7=models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_8=models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_9=models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_10=models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=now,blank=True)

    def __str__(self):
        return self.title
    

