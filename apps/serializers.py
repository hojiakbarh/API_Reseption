from rest_framework.serializers import ModelSerializer

from apps.models import User


class UserModelSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

