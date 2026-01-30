
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import registerSerializers

# Create your views here.

class RegisterApi(APIView):
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
