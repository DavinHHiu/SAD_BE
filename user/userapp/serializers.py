from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from userapp.models import User, FullName, Account, Address


class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = User
        fields = ["id", "email", "account"]

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, user, validated_data):
        password = validated_data.get("password", None)
        if password is not None:
            validated_data["password"] = make_password(password)
        user = super().update(user, validated_data)
        return user


class UserProfileSerialier(serializers.ModelSerializer):
    account = AccountSerializer()
    fullname = FullNameSerializer()
    address = AddressSerializer()

    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
