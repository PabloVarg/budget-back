from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.routers import Response


class MetricsViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["GET"])
    def test():
        return Response()
