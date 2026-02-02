"""Descargamos -djangorestframwork,djangorestframwork-simplejwt, django-cors-headers
metodos de solicitudes:
-get -> Genérico, pero no envía de forma encriptada.
-post -> Genérico, si sirve para encriptar.
-put -> Crear elementos y funciona a través de POST.
-patch -> Funciona con POST. Actualiza uno o varios valores pero no todos.
-delete -> Funciona con POST, solo que se usa solo para borrar datos.
"""
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Users.models import User
from Users.serializers import RegisterSerializer


class PruebaView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        usuarios = User.objects.all() # Con esta consulta tenemos un array de objetos de tipo usuario
        usuarios2 = User.objects.all().order_by("-first_name")
        # SELECT * FROM User WHERE is_active=True AND is_staff =True ORDER BY firs_name ASC
        usuarios3 = User.objects.filter(is_active=True, is_staff=True).order_by("-first_name")

#        data=[]
#        for usuario in usuarios:
#            data.append({"email":usuario.email, "first_name":usuario.first_name, "last_name":usuario.last_name, })
        data =[
            {"email": u.email, "first_name": u.first_name,
             "last_name": u.last_name,} for u in usuarios
        ]

        return Response({"success":True, "data": data}, status=status.HTTP_200_OK)

class RegisterView(APIView):
    permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]

    def post(self, request):
        #Para acceder a los elementos del body usamos request.data
        data = request.data
        #print(data)
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            print("Es valido")
            return Response({"success": True}, status=status.HTTP_200_OK)
        else:
            return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)