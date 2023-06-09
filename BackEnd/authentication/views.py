from .models import CustomUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import Token, RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)
        user = CustomUser.objects.get(email=str(attrs['email']))

        refresh = self.get_token(self.user)
        
        refresh['user_id'] = user.id
        refresh['first_name'] = user.first_name
        refresh['last_name'] = user.last_name
        refresh['email'] = user.email
        refresh['company'] = user.company.name
        refresh['company_is_active'] = user.company.is_active

        data = {
            'code': 0, 
            'type': "Técnico", 
            'message': "Credenciales validas", 
            'details': "ValidUser", 
            'data': {
                'refresh': str(refresh),
                "access": str(refresh.access_token)
                }, 
            'errors': [{
                "message": "Credenciales validas", 
                "details": "ValidUser"
            }]
        }

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
        except:
            raise InvalidUser({
                'code': 1, 
                'type': "Técnico", 
                'message': "Error de validación de usuario y contraseña", 
                'details': "InvalidUser", 
                'data': {}, 
                'errors': [{
                    "message": "Error de validación de usuario y contraseña", 
                    "details": "InvalidUser"
                }]
            })

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class InvalidUser(AuthenticationFailed):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = ("Credentials is invalid or didn't match")
    default_code = 'user_credentials_not_valid'