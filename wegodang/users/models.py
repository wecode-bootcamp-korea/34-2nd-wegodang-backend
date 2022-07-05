from django.db import models

class User(models.Model):
    username     = models.CharField(max_length=45, unique=True)
    first_name   = models.CharField(max_length=45, null=True)
    last_name    = models.CharField(max_length=45, null=True)
    email        = models.EmailField(max_length=200, unique=True)
    password     = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100, unique=True, null=True)
    kakao_id     = models.BigIntegerField()
    created_at   = models.DateField(auto_now_add=True)
    updated_at   = models.DateField()

    class Meta:
        db_table = 'users'

class Order(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    products_models = models.ForeignKey("products.ProductModel", on_delete=models.CASCADE, related_name="orders")
    address         = models.CharField(max_length=100)
    order_number    = models.CharField(max_length=100)

    class Meta:
        db_table = 'orders'