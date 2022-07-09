from django.test     import TestCase, Client
from products.models import Category, Product, ProductImage
from users.models    import User

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

class ProductViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        Category.objects.create(
            id   = 1,
            name = "카테고리"
        )

        User.objects.create(
            id         = 1,
            kakao_id   = 1,
            updated_at = "2022-01-02"
        )

        Product.objects.create(
            id             = 1,
            name           = "테스트",
            total_price    = 10,
            goal_price     = 10,
            suppoters      = 10,
            start_date     = "2022-01-01",
            end_date       = "2022-07-12",
            story          = "스토리",
            slide_title    = "슬라이더_타이틀",
            slide_subtitle = "슬라이더_서브타이틀",
            category       = Category.objects.get(id=1),
            user           = User.objects.get(id=1)
            )

        ProductImage.objects.create(
            id        = 1,
            product   = Product.objects.get(id=1),
            image_url = "테스트.url"
        )

    def tearDown(self):
        Category.objects.all().delete()
        User.objects.all().delete()
        Product.objects.all().delete()
        ProductImage.objects.all().delete()

    def test_success_get_product_details(self):
        response = self.client.get('/products/1')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(),
            {
                "products": {
                    "product_id"     : 1,
                    "product_name"   : "테스트",
                    "goal_percent"   : 100,
                    "total_price"    : 10,
                    "suppoters"      : 10,
                    "remaining_days" : 1,
                    "story"          : "스토리",
                    "image_url": [
                        {
                            "id"  : 1,
                            "url" : "테스트.url"
                        }
                    ]
                }
            }
        )