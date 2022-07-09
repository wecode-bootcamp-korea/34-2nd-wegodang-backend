import jwt
import json

from django.http      import JsonResponse
from django.views     import View

from products.models  import Category

class CategoryView(View):
    def get(self, request):

        result = {
            "categories" : list(Category.objects.values("id", "name", "image"))
        }

        return JsonResponse({"result" : result}, status=200)