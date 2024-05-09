
from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        # fields = '__all__'
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'created_at', 'updated_at')

    def validate(self, attrs):
        year_ = attrs['year']
        price_ = attrs['price']
        if year_ == price_:
            raise serializers.ValidationError({'details':f'{year_=}=={price_=}'})
        return attrs

    def validate_year(self, year):
        if year == 2003:
            raise serializers.ValidationError({'details':f'{year=}==2003'})
        return year