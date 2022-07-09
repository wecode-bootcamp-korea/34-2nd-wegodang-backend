from django.test import TestCase, Client
from products.models import Category

class CategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Category.objects.create(id=1, name="테스트", image="테스트.url")

    def tearDown(self):
        Category.objects.all().delete()

    def test_success_get_categories(self):
        response = self.client.get('/products/categories')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(),
        {
            "result": {
                "categories": [
                    {
                        "id"    : 1,
                        "name"  : "테스트",
                        "image" : "테스트.url"
                    }
                ]
            }
        }
        )