import jwt
import json

from django.http      import JsonResponse
from django.views     import View
from datetime         import date

from products.models  import Category, Product

class CategoryView(View):
    def get(self, request):

        result = {
            "categories" : list(Category.objects.values("id", "name", "image"))
        }

        return JsonResponse({"result" : result}, status=200)

class ProductView(View):
    def get(self, request, product_id):
        product = Product.objects.get(id = product_id)
        now     = date.today()

        product_images = product.product_images.all()

        product_images = [{
            "id"  : product_image.id,
            "url" : product_image.image_url
        } for product_image in product_images ]

        products = {
            "product_id"     : product.id,
            "product_name"   : product.name,
            "goal_percent"   : int(product.total_price / product.goal_price * 100),
            "total_price"    : int(product.total_price),
            "suppoters"      : product.suppoters,
            "remaining_days" : (product.end_date - now).days,
            "story"          : product.story,
            "image_url"      : product_images
        }
        
        return JsonResponse({"products": products}, status=200)
        
