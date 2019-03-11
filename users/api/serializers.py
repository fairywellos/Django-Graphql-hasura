from rest_framework import serializers
from users.models import UserProxy as User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'is_tenant',
            'password',
            'email',
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, attrs):
        super(UserSerializer, self).validate(attrs)
        is_tenant = attrs.get('is_tenant', None)
        username = attrs.get('username', None)
        if is_tenant and not username:
            raise serializers.ValidationError({'username': ['This field is required if user is a tenant.']})
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data, is_active=True)
