import jwt

from django.http  import JsonResponse

from users.models import User
from django.conf  import settings

def login_required(func):
    def wrapper(self,request,*args,**kwargs):
        try:
            client_token = request.headers.get("Authorization",None)
            payload      = jwt.decode(client_token, settings.SECRET_KEY, settings.ALGORITHM)
            user         = User.objects.get(id=payload['id'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : ['INVALID_TOKEN'] }, status=401)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status=401)

        return func(self, request, *args, **kwargs)
    return wrapper