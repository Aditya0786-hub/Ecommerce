from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class registerSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    
    class Meta:
        model = User
        fields = ['name','email','password','role','image']
        read_only_fields = ['id']
        
    def create(self,validated_data):
        user = User(
            name = validated_data['name'],
            email = validated_data['email'],
            role = validated_data['role'],
            image = validated_data.get('image')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)
    
    class Meta:
        model = User
        fields = ['email','password']
        
    def validate(self,data):
        user = authenticate(
            email= data["email"],
            password = data["password"]
        )
        
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        
        return user