from rest_framework import serializers
from django.contrib.auth.models import User
from drf_writable_nested.mixins import UniqueFieldsMixin
from adopet.models import Tutor

class UserSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def validate_username(self, username):
        if not username.isalpha():
            raise serializers.ValidationError('Username deve conter apenas letras')
        return username

class TutorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Tutor
        fields = ["id", "user", "phone", "city", "about"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)
        tutor = Tutor.objects.create(user=user, **validated_data)
        return tutor
    
    def update(self, instance, validated_data):
        if "user" in validated_data.keys():
            user_data = validated_data.pop("user")
            instance.user.username = user_data.get("username", instance.user.username)
            instance.user.password = user_data.get("password", instance.user.password)
            instance.user.email = user_data.get("email", instance.user.email)
            instance.user.save()

        instance.phone = validated_data.get("phone", instance.phone)
        instance.city = validated_data.get("city", instance.city)
        instance.about = validated_data.get("about", instance.about)
        instance.save()
        return instance
    
    def validate_phone(self, phone):
        if len(phone) != 11:
            raise serializers.ValidationError('Phone  deve ter 11 dígitos')
        return phone
    
    def validate_city(self, city):
        if not city.isalpha():
            raise serializers.ValidationError('City deve conter apenas letras')
        return city