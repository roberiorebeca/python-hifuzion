from django.test import TestCase
from rest_framework.test import APIClient

from hifuzion.contabilidade.models import Cliente, PlanoConta
from hifuzion.contabilidade.hooks import DrfApiCrudTest


class TestCliente(TestCase):
    def setUp(self):
        conta = PlanoConta(nome='William')
        conta.save()

        self.obj = Cliente()
        self.obj.nome = 'William Galleti'
        self.obj.fone = '9999999'
        self.obj.email = 'william@email.com'
        self.obj.conta_id = conta.id
        self.obj.save()

        post = dict(nome='William Galleti',
                    fone='9999999',
                    email='william@email.com',
                    conta=conta.id)

        put = dict(email='william@email.com')

        self.crud = DrfApiCrudTest(api_client=APIClient(),
                                   url='/contabilidade/clientes/',
                                   pk=self.obj.id,
                                   fields=['id', 'nome', 'fone', 'email', 'conta', 'conta_display'],
                                   add_dict=post,
                                   update_dict=post,
                                   test_class=self)

    def test_representation(self):
        self.assertEqual(str(self.obj), self.obj.nome)

    def test_api_crud(self):
        self.crud.testing()
