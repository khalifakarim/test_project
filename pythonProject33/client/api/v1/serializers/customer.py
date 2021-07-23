from core.serializers.base import SoftDeleteSerializer
from client.models import User


class UserSerializer(SoftDeleteSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'is_active',
            'password',
            'gender',
            'age',
        )
        read_only = ('id',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
