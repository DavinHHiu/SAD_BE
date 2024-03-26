from rest_framework import status
from rest_framework.views import APIView, Response

from mobilephone.models import MobilePhone
from mobilephone.serializers import MobilePhoneSerializer


class MobilePhoneListApiView(APIView):
    def get(self, request):
        mobile_phones = MobilePhone.objects.all()
        serializer = MobilePhoneSerializer(
            mobile_phones, many=True, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class MobilePhoneDetailApiView(APIView):
    def get_object(self, mobile_phone_id):
        try:
            return MobilePhone.objects.get(id=mobile_phone_id)
        except MobilePhone.DoesNotExist:
            return None

    def get(self, request, mobile_phone_id):
        mobile_phone = self.get_object(mobile_phone_id)
        if mobile_phone is not None:
            serializer = MobilePhoneSerializer(
                mobile_phone, context={"request": request}
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "Object with mobile_phone_id does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )
