import json
import jwt

from django.test   import TestCase, Client
from django.conf   import settings
from unittest.mock import patch, MagicMock

from users.models  import User

class LogInTest(TestCase):
    def setUp(self):
        User.objects.create(
            kakao_id  = 123456,
            user_name = "테스트_닉네임",
            email     = "test@naver.com"
        )

    def tearDown(self):
        User.objects.all().delete()

    @patch("users.views.requests")
    def test_kakao_login_get_success(self, mocked_requests):
        client = Client()

        class MockedResponse:
            status_code = 200

            def json(self):
                return {
                        "id"            : 2145645622,
                        "properties"    : {"nickname" : "test"},
                        "kakao_account" : {"email" : "test@gmail.com"}
                    }

        mocked_requests.get = MagicMock(return_value = MockedResponse())
        headers             = {"Authoriazation": "123456"}
        response            = client.get("/users/kakao", **headers)

        self.assertEqual(response.status_code, 200)

    def test_kakao_signup_post_success(self):
        client = Client()

        user = {
            "kakao_id"  : 123457,
            "user_name" : "kws",
            "email"     : "kws@naver.com"
        }

        response = client.post('/users/kakao', json.dumps(user), content_type = 'application/json')
        
        token = jwt.encode({'id': User.objects.get(kakao_id=123457).id}, settings.SECRET_KEY, settings.ALGORITHM)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(),{
            "message" : "CREATE_ACCOUNT",
            "token"   : token
        })

    def test_kakao_login_post_success(self):
        client = Client()

        user = {
            "kakao_id"  : 123456,
            "user_name" : "테스트_닉네임",
            "email"     : "test@naver.com"
        }

        response = client.post('/users/kakao', json.dumps(user), content_type = 'application/json')

        token = jwt.encode({'id': User.objects.get(kakao_id=123456).id}, settings.SECRET_KEY, settings.ALGORITHM)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
            "message" : "LOGIN_SUCCESS",
            "token"   : token
        })

    def test_user_detail_view_invalid_token(self):
        client = Client()        
        
        headers = {"Authorization":"가짜_token"}
        
        response = client.get('/users/kakao', content_type='application/json', **headers)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'INVALID_RESPONSE'})

    def test_kakao_login_keyerror(self):
        client = Client()

        user = {
            "kakao_id" : 12345612345
        }
        
        response = client.post('/users/kakao', json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message" : "KEYERROR"})