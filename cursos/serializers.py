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

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):  # 1,2,3,4,5
            return valor
        raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5.')


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinks Related Fields
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='avaliacao-detail')

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'publicacao',
            'atualizacao',
            'ativo',
            'avaliacoes'
        )
