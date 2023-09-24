from rest_framework import serializers

from movements.models import Movement


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = "__all__"
