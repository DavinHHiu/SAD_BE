from rest_framework import status
from rest_framework.views import APIView, Response

from cloth.models import Cloth
from cloth.serializers import ClothSerializer


class ClothListApiView(APIView):
    def get(self, request):
        clothes = Cloth.objects.all()
        serializer = ClothSerializer(clothes, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClothDetailApiView(APIView):
    def get_object(self, cloth_id):
        try:
            return Cloth.objects.get(id=cloth_id)
        except Cloth.DoesNotExist:
            return None

    def get(self, request, cloth_id):
        cloth = self.get_object(cloth_id)
        if cloth is not None:
            serializer = ClothSerializer(cloth, context={"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "Object with cloth_id does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )
