from rest_framework import serializers
from ..models import Carlist

def alphanumeric(value):
    if not str(value).isalnum():
        raise serializers.ValidationError("Only alphanumeric characters are allowed")

class CarSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField(read_only=True)
    registration_number = serializers.CharField(validators = [alphanumeric])
    price = serializers.DecimalField(max_digits=9, decimal_places=2)

    def create(self, validated_data):
        return Carlist.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.active = validated_data.get("active", instance.active)
        instance.registration_number = validated_data.get("registration_number", instance.registration_number)
        instance.price = validated_data.get("price", instance.price)
        instance.save()
        return instance
    
    def validate_data(self, value):
        if value <= 20000.00:
            raise serializers.ValidationError("Price must be greater than 20000.00")
        return value
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description must be different")
        return data