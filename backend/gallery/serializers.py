from rest_framework import serializers
from .models import Image
from django.db import models


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "title", "image", "order"]
        extra_kwargs = {"order": {"required": False}}

    def update(self, instance, validated_data):
        current_order = instance.order
        new_order = validated_data.get("order", current_order)

        if new_order != current_order:
            if new_order > current_order:
                Image.objects.filter(
                    order__gt=current_order, order__lte=new_order
                ).update(order=models.F("order") - 1)
            else:
                Image.objects.filter(
                    order__gte=new_order, order__lt=current_order
                ).update(order=models.F("order") + 1)

            instance.order = new_order

        instance = super().update(instance, validated_data)

        return instance
