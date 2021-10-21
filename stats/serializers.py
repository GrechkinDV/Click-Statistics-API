from rest_framework.serializers import ModelSerializer

from .models import ClickStatistic


class ClickStatisticSerializer(ModelSerializer):
    class Meta:
        model = ClickStatistic
        fields = "__all__"
        read_only_fields = ["date", "cpc", "cpm"]

    def create(self, validated_data):
        """ Create a Click Static """
        return ClickStatistic.objects.create_click_statistic(**validated_data)
