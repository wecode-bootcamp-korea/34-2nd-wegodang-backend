import jwt
import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q
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
            "start_date"     : product.start_date,
            "end_date"       : product.end_date,
            "remaining_days" : (product.end_date - now).days,
            "story"          : product.story,
            "image_url"      : product_images
        }
        
        return JsonResponse({"products": products}, status=200)

class ProductListView(View):
    def get(self, request):
        category = request.GET.get('category_id')
        offset   = int(request.GET.get('offset', 0))
        limit    = int(request.GET.get('limit', 5))
        order    = request.GET.get('order')
        now      = date.today()

        q = Q()

        if category:
            q &= Q(category_id=category)

        order_set = {
            'id'     : 'id',
            'random' : '?'
        }

        order_field = order_set.get(order, 'id')
        
        products = Product.objects.filter(q).order_by(order_field)[offset:offset+limit]

        products = [{
            "product_id"     : product.id,
            "product_name"   : product.name,
            "category_name"  : product.category.name,
            "user"           : product.user.user_name,
            "goal_percent"   : int(product.total_price / product.goal_price * 100),
            "goal_price"     : int(product.goal_price),
            "remaining_days" : (product.end_date - now).days,
            "image_url"      : product.product_images.first().image_url,
            "slide_title"    : product.slide_title,
            "slide_subtitle" : product.slide_subtitle
            } for product in products]

        return JsonResponse({"products" : products}, status=200)
