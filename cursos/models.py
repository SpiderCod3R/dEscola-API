from django.db import models

# Classe Modelo Abstrato
class Base(models.Model):
    publicacao = models.DateTimeField(auto_now=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=225)
    url = models.URLField(unique=True)

    class Meta:
            verbose_name = 'Curso'
            verbose_name_plural = 'Cursos'
            ordering = ['id']

    def __str__(self):
        return self.titulo


class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.FloatField()

    class Meta:
        verbose_name = 'avaliacao'
        verbose_name_plural = 'avaliacoes'
        unique_together = ('email', 'curso') # Cada pessoa com o mesmo email nao pode avaliar mais de uma vez
        ordering = ['id']

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'