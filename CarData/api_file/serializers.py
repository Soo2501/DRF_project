from rest_framework import serializers 
from ..models import Carlist, Showroomlist, Review

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields= '__all__'


class CarSerializers(serializers.ModelSerializer):
    Reviews = ReviewSerializers(many=True, read_only=True)
    discounted_price = serializers.SerializerMethodField()   
    class Meta:
        model = Carlist
        fields = '__all__'

    def get_discounted_price(self, object):
       discountprice = object.price - 5000
       return discountprice

    def validate_data(self, value):
        if value <= 20000.00:
            raise serializers.ValidationError("Price must be greater than 20000.00")
        return value
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description must be different")
        return data
    
class ShowroomSerializers(serializers.ModelSerializer):
    # Showrooms = CarSerializers(many=True, read_only=True )
    # Showrooms =  serializers.StringRelatedField(many=True)

    class Meta:
        model = Showroomlist
        fields = "__all__"


