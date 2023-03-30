from . models import user
from rest_framework import serializers


class userserializer(serializers.ModelSerializer):
    # first_name = models.CharField(max_length=100, blank=False)
    # last_name = models.CharField(max_length=100, blank=True)
    # email = models.CharField(max_length=100, unique=True, blank=False)
    # phone_number = models.CharField(max_length=20, blank=False)
    # address = models.CharField(max_length=200, blank=False)
    # pincode = models.CharField(max_length=6, blank=False)
    # company_name = models.CharField(max_length=50, blank=False)

    class Meta:
        model = user
        fields='__all__'
        extra_kwargs ={
            'password':{"write_only":True}
        }

    def create(self,validated_data):
        password =validated_data.pop('password',None)
        instance = self.Meta.model([validated_data])

        if password is not None:
            instance.set_password((password))
        instance.save()
        return  instance