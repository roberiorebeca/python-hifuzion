from rest_framework import serializers
from hifuzion.contabilidade.models import Cliente, PlanoConta, Todo


class PlanoContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoConta
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    conta_display = serializers.SerializerMethodField()

    def get_conta_display(self, obj: Cliente):
        return obj.conta.nome

    class Meta:
        model = Cliente
        fields = '__all__'
        

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'