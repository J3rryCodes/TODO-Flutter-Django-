from rest_framework.serializers import ModelSerializer
from core.models import UserProfileModel


class UserProfileSerializer(ModelSerializer):
    """ Serializer for UserProfileModel """

    class Meta:
        model = UserProfileModel
        fields = ['email','is_staff','name','password','is_active']

        extra_kwargs = {
            'password' : {'write_only':True},
            'is_staff' : {'read_only':True},
            'is_active' : {'read_only':True}
        }

    def create(self,validated_data):
        user = UserProfileModel.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user