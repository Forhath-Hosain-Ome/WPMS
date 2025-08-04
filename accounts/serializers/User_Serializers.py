from rest_framework import serializer
from accounts.models import UserModel

class UserSerializer(serializer.ModelSerializers):
    class Meta:
        model = UserModel
        fields = '__all__'