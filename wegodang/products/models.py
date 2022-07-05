from django.db import models

class Category(models.Model):
    name  = models.CharField(max_length=45)
    image = models.CharField(max_length=200)

    class Meta:
        db_table = 'catergories'

class Product(models.Model):
    name           = models.CharField(max_length=45)
    total_pirce    = models.DecimalField(max_digits=10, decimal_places=2)
    goal_pirce     = models.DecimalField(max_digits=10, decimal_places=2)
    suppoters      = models.IntegerField()
    start_date     = models.DateField()
    end_date       = models.DateField()
    story          = models.TextField()
    slide_title    = models.TextField()
    slide_subtitle = models.TextField()
    category       = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    class Meta:
        db_table = 'products'

class ProductModel(models.Model):
    name    = models.CharField(max_length=45)
    price   = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_models")

    class Meta:
        db_table = 'product_models'

class ProductImage(models.Model):
    product   = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image_url = models.CharField(max_length=200)

    class Meta:
        db_table = 'product_images'