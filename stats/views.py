from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import ClickStatistic
from .serializers import ClickStatisticSerializer


class ClickStatisticViewset(ModelViewSet):
    """
    A model viewset for ClickStatistic model object.
    Used to create, display, delete objects
    """
    serializer_class = ClickStatisticSerializer
    http_method_names = ["get", "post", "delete"]

    def get_queryset(self):
        """
        Get listed queryset by filtering date range
        param from: from which date inclusive
        type from: date YYYY-MM-DD
        param to: to which date inclusive
        type to: date YYYY-MM-DD
        """
        if self.kwargs.get('pk'):
            return self.get_queryset_detail()
        try:
            if(self.request.GET["from"] is None or self.request.GET["to"] is None):
                raise ValidationError(
                    "Parameters 'from' and 'to' must be set!", 400)
        except MultiValueDictKeyError:
            raise ValidationError(
                "Parameters 'from' and 'to' must be set!", 400)

        try:
            return ClickStatistic.objects.filter(date__range=[self.request.GET["from"], self.request.GET["to"]])
        except Exception as e:
            raise ValidationError(
                "Parameters 'from' and 'to' must be properly set in format(YYYY-MM-DD)!", 400)

    def get_queryset_detail(self):
        """ 
        Detail view
        """
        return ClickStatistic.objects.filter(id=self.kwargs.get("pk"))

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        ClickStatistic.objects.all().delete()
        return Response("All deleted", status=status.HTTP_204_NO_CONTENT)
