
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import registerSerializers
from .serializers import LoginSerializer
from rest_framework.permissions import IsAuthenticated
from .utils import get_access_tokens

# Create your views here.

class RegisterApi(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request):
        serializer = registerSerializers(data = request.data) # Here we check the data is valid through serializeres
        
        if serializer.is_valid():
            user = serializer.save() # Here we create the new user insatnce of user model
            user_data = registerSerializers(user).data # here we convert it into json and only send allowed fields
            return Response(
                {
                    "user": user_data,
                    "message": "user is created"
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# Login Api
class LoginApi(APIView):
    #Json data to python objects
    # Check its validation
    # check the user and pass matches
    #Create Access Token and refesh
    #return response
    
    permission_classes = [AllowAny]
    
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data
        tokens = get_access_tokens(user)
        
        response =  Response(
            {
                "message": "Login Successfull",
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "role": user.role
                }
            },
            status= status.HTTP_200_OK
        )
        
        response.set_cookie(
            key="access_token",
            value=tokens["access"],
            httponly=True,
            secure=False,      
            samesite="Lax"
        )

        response.set_cookie(
            key="refresh_token",
            value=tokens["refresh"],
            httponly=True,
            secure=False,
            samesite="Lax"
        )

        return response

class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response(
            {"message": "Logged out successfully"},
            status=status.HTTP_200_OK
        )

        # delete cookies
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        return response