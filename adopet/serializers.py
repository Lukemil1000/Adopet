from rest_framework import serializers
from drf_writable_nested.mixins import UniqueFieldsMixin
from adopet.models import Shelter, Tutor, Pet, Adoption, Account
import re
from pycpfcnpj import cnpj as cnpj_validator
from pycpfcnpj import cpf as cpf_validator

class AccountSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "username", "password", "email", "name", "phone", "adress", "about", "user_type"]
        extra_kwargs = {
            'password': {'write_only': True},
            'user_type': {'read_only': True},
        }

    def validate_name(self, name):
        if bool(re.search(r"\d", name)):
            raise serializers.ValidationError('Name não pode conter números')
        return name

    def validate_phone(self, phone):
        if len(phone) != 11:
            raise serializers.ValidationError('Phone deve ter 11 dígitos')
        return phone

class TutorSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = Tutor
        fields = ["id", "cpf", 'account']

    def create(self, validated_data):
        account_data = validated_data.pop("account")
        account = Account.objects.create_user(user_type='tutor', **account_data)
        tutor = Tutor.objects.create(account=account, **validated_data)
        return tutor
    
    def update(self, instance, validated_data):
        if "account" in validated_data.keys():
            account_data = validated_data.pop("account")
            instance.account.username = account_data.get("username", instance.account.username)
            instance.account.set_password(account_data.get("password", instance.account.password))
            instance.account.email = account_data.get("email", instance.account.email)
            instance.account.name = account_data.get("name", instance.account.name)
            instance.account.phone = account_data.get("phone", instance.account.phone)
            instance.account.adress = account_data.get("adress", instance.account.adress)
            instance.account.about = account_data.get("about", instance.account.about)
            instance.account.save()

        instance.cpf = validated_data.get("cpf", instance.cpf)
        instance.save()
        return instance
    
    def validate_cpf(self, cpf):
        if not cpf_validator.validate(cpf):
            raise serializers.ValidationError('CPF inválido')    
        return cpf
    
class ShelterSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = Shelter
        fields = ["id", "cnpj", 'account']
    
    def create(self, validated_data):
        account_data = validated_data.pop("account")
        account = Account.objects.create_user(user_type='shelter', **account_data)
        shelter = Shelter.objects.create(account=account, **validated_data)
        return shelter
    
    def update(self, instance, validated_data):
        if "account" in validated_data.keys():
            account_data = validated_data.pop("account")
            instance.account.username = account_data.get("username", instance.account.username)
            instance.account.set_password(account_data.get("password", instance.account.password))
            instance.account.email = account_data.get("email", instance.account.email)
            instance.account.name = account_data.get("name", instance.account.name)
            instance.account.phone = account_data.get("phone", instance.account.phone)
            instance.account.adress = account_data.get("adress", instance.account.adress)
            instance.account.about = account_data.get("about", instance.account.about)
            instance.account.save()

        instance.cnpj = validated_data.get("cnpj", instance.cnpj)
        instance.save()
        return instance

    def validate_cnpj(self, cnpj):
        if not cnpj_validator.validate(cnpj):
            raise serializers.ValidationError('CNPJ inválido')    
        return cnpj
    
class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ["id", "shelter", "name", "description", "adopted", "age"]
        read_only_fields = ["adopted",]
    
    def validate_name(self, name):
        if bool(re.search(r"\d", name)):
            raise serializers.ValidationError('Name não pode conter números')
        return name
    
class AdoptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adoption
        fields = ["id", "pet", "tutor", "date"]