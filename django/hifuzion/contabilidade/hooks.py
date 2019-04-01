import random

from django.test import TestCase
from rest_framework.test import APIClient


class DrfApiCrudTest:
    """
    Crud api for testing basic http verbs
    Use sample:

    class TestExample(TestCase):
        def setUp(self):
            self.obj = Example()
            self.obj.name = 'William Galleti'
            self.obj.title = 'Mr.'
            self.obj.save()
            self.crud = DrfApiCrudTest(api_client=APIClient(),
                                       url='/api/examples/',
                                       pk=self.obj.id,
                                       fields=['id', 'name', 'title'],
                                       add_dict=dict(name='William', title='Mr.'),
                                       update_dict=dict(name='William Galleti', title='Mrs.'),
                                       test_class=self)

        def test_representation(self):
            self.assertEqual(str(self.obj), self.obj.name)

        def test_api_crud(self):
            self.crud.testing()
    """

    def __init__(self, api_client: APIClient, url, pk, fields, add_dict, update_dict, test_class: TestCase):
        """
        Constructor for testing
        :param api_client: Class drf API client for call http verbs
        :param url: Base url for endpoint
        :param pk: Key using on get unique instance and check fields
        :param fields: The fields that will be checked
        :param add_dict: Data will be insert on post verb
        :param update_dict: Data will be update on put and patch verbs
        :param test_class: Django class test (TestCase)
        """
        self.test_class = test_class
        self.api_client = api_client
        self.url = url
        self.pk = pk
        self.fields = fields
        self.add_dict = add_dict
        self.update_dict = update_dict
        self.add_response = None

    def get_status(self):
        """
        Testing get return status code 200
        """
        request = self.api_client.get(self.url)
        self.test_class.assertEqual(request.status_code, 200)

    def get_fields(self):
        """
        Testing get unique return expected fields
        """
        request = self.api_client.get(f'{self.url}{self.pk}/')
        if request.status_code != 200:
            return self.test_class.fail(f'Get fail. Status code {request.status_code}')
        response = request.data

        for field in self.fields:
            self.test_class.assertIn(field, response)

    def post_status(self):
        """
        Testing post return status code 201 (added successfully)
        """
        post = self.add_dict
        request = self.api_client.post(self.url, post, format='json')

        if request.status_code == 201:
            self.add_response = request.data
        else:
            self.test_class.fail(f'Error on post_add. {request.content}')
        self.test_class.assertEqual(request.status_code, 201)

    def put_status(self):
        """
        Testing put return status code 200 (updated all fields successfully)
        """
        put = self.update_dict
        request = self.api_client.put(f'{self.url}{self.add_response["id"]}/', put, format='json')
        self.test_class.assertEqual(request.status_code, 200)

    def patch_status(self):
        """
        Testing path return status code 200 (updated one or more fields successfully)
        """
        random_key = random.randrange(0, len(self.update_dict))
        dict_key = list(enumerate(self.update_dict))[random_key][1]
        patch = {dict_key: self.update_dict[dict_key]}
        request = self.api_client.patch(f'{self.url}{self.add_response["id"]}/', patch, format='json')
        self.test_class.assertEqual(request.status_code, 200)

    def delete_status(self):
        """
        Testing delete return status code 204
        """
        request = self.api_client.delete(f'{self.url}{self.add_response["id"]}/', {}, format='json')
        self.test_class.assertEqual(request.status_code, 204)

    def testing(self):
        """
        Running all tests
        """
        self.get_status()
        self.get_fields()
        self.post_status()
        self.put_status()
        self.patch_status()
        self.delete_status()
