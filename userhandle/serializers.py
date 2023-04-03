from . models import user
from rest_framework import serializers
from django.db import models

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields=['id','first_name','last_name','email','phone_number','address','pincode','company_name','password']
        extra_kwargs ={
            'password':{"write_only":True}
        }

    def create(self,validated_data):
        password =validated_data.pop('password',None)
        instance = self.Meta.model([validated_data])

        if password is not None:
            instance.set_password((password))
        instance.save()
        return instance