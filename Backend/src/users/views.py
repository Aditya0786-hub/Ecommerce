
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class TestApi(APIView):
    def get(self, request):
        return Response(
            {
                "status": "success",
                "message": "Djnago resr is working"
            },
        )
