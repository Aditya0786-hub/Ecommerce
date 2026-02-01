from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

def get_access_tokens(user):
    refresh = RefreshToken.for_user(user)
    
    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh)
    }

