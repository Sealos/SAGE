from rest_framework.views import APIView

estacionamientos = ()

class EstacionamientoView(APIView):
    def get(self, request):
        pass

class EstacionamientosView(APIView):
    def get(self, request, _id):
        pass