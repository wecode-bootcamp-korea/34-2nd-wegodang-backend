from msilib.schema import Error
import jwt
import requests
import json

from django.http            import JsonResponse
from django.core.exceptions import ValidationError
from django.views           import View
from django.conf            import settings

from users.models           import User
from users.validator        import validate_email

class KakaoAPI():
    def __init__(self, KAKAO_REST_KEY):
        self.KAKAO_REST_KEY = KAKAO_REST_KEY

    def get_user_information(self, token):
        KAKAO_INFO_API = 'https://kapi.kakao.com/v2/user/me'
        response       = requests.get(KAKAO_INFO_API, headers={'Authorization': f'Bearer {token}'}, timeout=5)
        
        if not response.ok:
            raise Error 

        user_information = response.json()
        return user_information

    def get_map_information(self):
        pass

    def check_kakao_user(self, token):
        return True | False


class KaKaoSignUpView(View):
    def get(self, request):
        access_token = request.headers.get('Authorization')
        kakao_api    = KakaoAPI(settings.KAKAO_REST_KEY)
        
        user_information = kakao_api.get_user_information(access_token)
        kakao_id         = user_information['id']
        user_name        = user_information['properties']['nickname']
        email            = user_information['kakao_account']['email']
        is_user          = False

        is_user          = User.objects.filter(kakao_id = kakao_id).exists()

        result = {
            'kakao_id'  : kakao_id,
            'user_name' : user_name,
            'email'     : email,
            'is_user'   : is_user
        }

        return JsonResponse({'result' : result }, status = 200)
    
    def post(self, request): 
        try:
            data = json.loads(request.body)

            validate_email(data['email'])

            user, is_created = User.objects.update_or_create(
                kakao_id = data['kakao_id'],
                defaults = {
                    'user_name' : data['user_name'],
                    'email'     : data['email']
                }
            )
        
            status       = 201 if is_created else 200
            message      = 'CREATE_ACCOUNT' if is_created else 'LOGIN_SUCCESS'
            client_token = jwt.encode({'id':user.id}, settings.SECRET_KEY, settings.ALGORITHM)
        
            return JsonResponse({'message': message, 'token': client_token}, status=status)

        except ValidationError as error:
            return JsonResponse({"message" : error.message}, status = 400)

        except KeyError:
            return JsonResponse({"message" : "KEYERROR"}, status = 400)