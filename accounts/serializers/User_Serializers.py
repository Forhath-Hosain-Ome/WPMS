
from accounts.models import UserModel

class UserSerializer(serializers.ModelSerializers):
    class Meta:
        model = UserModel
        fields = '__all__'