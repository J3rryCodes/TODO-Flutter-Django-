from rest_framework.serializers import ModelSerializer
from todo_api.models import TODOModel


class TODOModelSeralizer(ModelSerializer):
    """Seralizer for TODO model"""

    class Meta:
        model = TODOModel
        fields = ['id','title','description','date','is_completed']