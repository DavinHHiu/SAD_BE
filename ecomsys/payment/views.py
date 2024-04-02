from payment.models import Payment
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class PaymentMethodListApiView(APIView):
    def get(self, request, *args, **kwargs):
        response = {
            "payment_methods": Payment.payment_choices_list,
        }
        return Response(response, status=status.HTTP_200_OK)
