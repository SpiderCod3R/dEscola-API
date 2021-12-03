from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'publicacao',
            'atualizacao',
            'ativo',
        )


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'titulo': {'write_only': True}
        }
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'publicacao',
            'atualizacao',
            'ativo',
        )