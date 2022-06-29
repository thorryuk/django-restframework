from rest_framework import serializers
from .models import Divisi

class DivisiSerializer(serializers.ModelSerializer):
    reseller_id = serializers.IntegerField()
    id_divisi = serializers.CharField(max_length=50)
    nama_divisi = serializers.CharField(max_length=75)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


    class Meta:
        model = Divisi
        fields = ('__all__')
