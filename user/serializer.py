from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegisterSerailzer(serializers.ModelSerializer):
    confrim_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','confrim_password','email']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        email = self.validated_data['email']
        last_name = self.validated_data['last_name']
        password = self.validated_data['password']
        pasword1 = self.validated_data['confrim_password']

        if password != pasword1:
            raise serializers.ValidationError({"errors":"Password Don't Match !"})
        
        # if User.objects.filter(email=email).exists():
        #     raise serializers.ValidationError({"errors":"Already Email Match !"})
        
        account = User(username=username,first_name=first_name,last_name=last_name,email=email)
        print(account)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account
        

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


    
