from rest_framework import serializers
from django.contrib.auth import get_user_model

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