from rest_framework import serializers
from src.fifo_user.models import UserDetail

class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDetail
        fields = [
            'userID',     
            'role',       
            'username',   
            'first_name', 
            'last_name',  
            'dob',        
            'email', 
            'password',     
            'userphone',  
            'useraddress',
            'Image',
        ]

    def create(self, validated_data):
        
        password = validated_data.pop('password', None)
        user_obj = self.Meta.model(**validated_data)
       
        user_obj.set_password(password)
        # import pdb
        # pdb.set_trace()
        user_obj.isActivated = True
        user_obj.save()
        user_obj.save()
        return user_obj

class UserUpdateSertializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = [
            'userID',     
            'role',       
            'username',   
            'first_name', 
            'last_name',  
            'dob',        
            'email',      
            'userphone',  
            'useraddress',
        ]
    
    def update(self, instance, validated_data):
        instance.role = validated_data.get('role', instance.role)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.email = validated_data.get('email', instance.email)
        instance.userphone = validated_data.get('userphone', instance.userphone)
        instance.useraddress = validated_data.get('useraddress', instance.useraddress)
        instance.save()
    
        user_obj = UserDetail.objects.get(
                userID=instance.userID
            )

        return user_obj