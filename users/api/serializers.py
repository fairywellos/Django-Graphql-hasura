from rest_framework import serializers
from users.models import UserProxy as User


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'is_tenant',
            'password',
            'confirm_password',
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
        password = attrs.get('password', None)
        confirm_password = attrs.get('confirm_password', None)
        errors = dict()
        if password != confirm_password:
            errors.update({'confirm_password': 'Passwords do not match', 'password': 'Passwords do not match'})
        if is_tenant and not username:
            errors.update({'username': ['This field is required if user is a tenant.']})
        if bool(errors):
            raise serializers.ValidationError(errors)
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data, is_active=True)
