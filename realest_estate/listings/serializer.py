from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields=('title','address','city','state','price','sale_type','house_type','bedrooms','sqft','photo_main','slug')
class ListingdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Listing
        fields="__all__"
        Lookup_field='slug'
    