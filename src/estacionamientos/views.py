from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

estacionamientos = ()

class EstacionamientoView(APIView):
    def get(self, request):
        return Response("Yes", status=status.HTTP_200_OK)
    def post(self, request):
        pass

class EstacionamientosView(APIView):
    def get(self, request, _id):
        return Response("Yes " + _id, status=status.HTTP_200_OK)