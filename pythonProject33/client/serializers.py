from rest_framework import serializers

from client.models import User


class UserSerializer(serializers.ModelSerializer):
    username = None

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'id',
            'balance',
            'age',
            'gender',
            'birthday',
        )

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            balance=validated_data['balance'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            birthday=validated_data['birthday'],

        )

        user.set_password(validated_data['password'])
        user.save()
        return user
