from typing import Dict
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        write_only=True,
        required=True,
        min_length=6,
        )
    
    class Meta:
        model = User
        fields = ["username", "email", "password", "password_confirm"]
        
    def validate(self, attrs: Dict[str, str]) -> Dict[str, str]:
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm")
        
        if password != password_confirm:
            raise serializers.ValidationError("Password do not match!")
        return attrs
    
    def create(self, validated_data: Dict[str, str]) -> User:
        user = User.objects.create_user(**validated_data)
        return user