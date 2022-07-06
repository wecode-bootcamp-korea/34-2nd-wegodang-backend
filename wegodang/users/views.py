from os import access
import jwt
import requests
import json

from django.http import JsonResponse
from django.views import View
from django.conf import settings

from users.models import User
from products.models import User

class KaKaoLoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            access_token   = data['access_token']
            KAKAO_INFO_API = 'https://kapi.kakao.com/v2/user/me'
            user_info      = requests.get(KAKAO_INFO_API, headers={'Authorization': f'Bearer {access_token}'}).json()
            print(user_info)
            kakao_id       = user_info['id']
            name           = user_info['properties']['nickname']
            email          = user_info['kakao_account']['email']

            user, created = User.objects.get_or_create(
                kakao_id = kakao_id,
                defaults = {
                    'username' : name,
                    'email' : email, 
                    }
                )

            success_status = 201 if created else 200
            message = 'LOGIN_SUCCESS'
            wegodang_token = jwt.encode({"id" : user.id}, settings.SECRET_KEY, algorithm = settings.ALGORITHM)

            return JsonResponse({"message" : message, 'token' : wegodang_token}, status = success_status)

        except:
            return JsonResponse({"message" : "KEYERROR"}, status = 400)