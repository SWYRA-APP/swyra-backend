from rest_framework import serializers
from .models import Designer, BuyerRequest

class DesignerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Designer
        fields = [
            'first_name',
            'last_name',
            'business_name',
            'email',
            'location',
            'specialty',
            'password',
            'confirm_password',
        ]

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')
        user = Designer.objects.create_user(
            password=password,
            **validated_data
        )
        return user


class DesignerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        from django.contrib.auth import authenticate
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        return {
            'email': user.email,
            'business_name': user.business_name
        }


class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = [
            'id',
            'first_name',
            'last_name',
            'business_name',
            'email',
            'location',
            'specialty',
        ]


class BuyerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerRequest
        fields = [
            'id',
            'phone',
            'location',
            'category',
            'description',
            'timestamp',
        ]
