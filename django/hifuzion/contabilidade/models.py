from django.db import models


class PlanoConta(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=80)
    fone = models.CharField(max_length=20)
    email = models.EmailField()
    conta = models.ForeignKey(to='contabilidade.PlanoConta', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Todo(models.Model):
    cliente = models.ForeignKey(to='contabilidade.Cliente', on_delete=models.CASCADE)
    nota = models.TextField()
    finalizado = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nota

    def finalizar(self):
        self.finalizado = True
        self.save()
