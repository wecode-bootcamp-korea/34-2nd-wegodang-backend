import jwt
import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from products.models  import Category, Product, ProductModel, ProductImage

class ProductListView(View):
    def get(self, request):
        category = request.GET.get('category_id')
        offset   = int(request.GET.get('offset', 0))
        limit    = int(request.GET.get('limit', 5))

        q = Q()

        if category:
            q &= Q(category_id=category)

        products = Product.objects.filter(q)[offset:offset+limit]

        products = [{
            "product_id"     : product.id,
            "product_name"   : product.name,
            "category_name"  : product.category.name,
            "user"           : product.user.user_name,
            "goal_percent"   : int(product.total_price / product.goal_price * 100),
            "goal_price"     : int(product.goal_price),
            "remaining_days" : (product.end_date - product.start_date.today()).days,
            "image_url"      : product.product_images.first().image_url
            } for product in products ]

        return JsonResponse({"products": products}, status=200)