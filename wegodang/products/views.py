import jwt
import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from products.models  import Category, Product, ProductModel, ProductImage

class SliderView(View):
    def get(self, request):

        products = Product.objects.order_by('?')[0:8]

        products = [{
            "image_url"      : product.product_images.first().image_url,
            "slide_title"    : product.slide_title,
            "slide_subtitle" : product.slide_subtitle
        } for product in products]

        return JsonResponse({"products": products}, status=200)