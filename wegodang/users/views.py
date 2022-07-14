import jwt
import requests
import json
import boto3
import uuid

from django.http            import JsonResponse
from django.core.exceptions import ValidationError
from django.views           import View
from django.conf            import settings

from users.models           import User
from users.validator        import validate_email
from users.utils            import login_required
from storage                import s3_file_uploader

class KaKaoSignUpView(View):
    def get(self, request):
        access_token     = request.headers.get('Authorization')
        KAKAO_INFO_API   = 'https://kapi.kakao.com/v2/user/me'
        response         = requests.get(KAKAO_INFO_API, headers={'Authorization': f'Bearer {access_token}'}, timeout=5)

        if not response.ok:
            return JsonResponse({'message' : 'INVALID_RESPONSE' }, status = 400)

        user_information = response.json()
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

class ProfileView(View):
    @login_required
    def post(self, request):
        try:
            file              = request.FILES.get('file')
            profile_image_url = s3_file_uploader.upload(file)
            user              = request.user

            if not profile_image_url:
                return JsonResponse({'message' : 'FILE_UPLOAD_ERROR'}, status=400)

            User.objects.filter(id=user.id).update(profile_image = profile_image_url)

            return JsonResponse({"message" : "UPLOAD_SUCCESS"}, status=201)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

    @login_required
    def get(self, request):
        user = request.user

        user_info = {
            "user_id"       : user.id,
            "user_name"     : user.user_name,
            "email"         : user.email,
            "profile_image" : user.profile_image
        }

        return JsonResponse({"user_info": user_info}, status=200)