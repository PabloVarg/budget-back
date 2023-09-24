from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from movements.models import Movement
from movements.serializers import MovementSerializer


class MovementViewSet(viewsets.ModelViewSet):
    serializer_class = MovementSerializer
    queryset = Movement.objects.all()

    @action(detail=False, methods=["GET"])
    def categories(self, request):
        return Response(
            Movement.objects.order_by().values_list("category", flat=True).distinct()
        )
