from django.db import models

class User(models.Model):
    user_name     = models.CharField(max_length=45, unique=True)
    email         = models.EmailField(max_length=200, unique=True)
    kakao_id      = models.BigIntegerField()
    profile_image = models.CharField(max_length=200, default="https://cdn.pixabay.com/photo/2017/09/10/18/25/question-2736480_1280.jpg")
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

class Order(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    products_models = models.ForeignKey("products.ProductModel", on_delete=models.CASCADE, related_name="orders")
    address         = models.CharField(max_length=100)
    order_number    = models.CharField(max_length=100)

    class Meta:
        db_table = 'orders'