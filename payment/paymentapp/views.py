from paymentapp.models import Payment
from paymentapp.serializers import PaymentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class PaymentMethodListApiView(APIView):
    def get(self, request, *args, **kwargs):
        response = {
            "payment_methods": Payment.payment_choices_list,
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        action = request.data.get("action")
        order_id = request.data.get("order_id")

        if action == "add":
            total_price = request.data.get("total_price")
            payment = Payment(order_id=order_id, total_price=total_price)
            payment.save()
        elif action == "get":
            payment = Payment.objects.filter(order_id=order_id).first()

        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        payment_id = request.data.get("payment_id")
        payment_method = request.data.get("payment_method")
        total_price = request.data.get("total_price")

        payment = Payment.objects.get(id=payment_id)
        if payment_method:
            payment.payment_method = payment_method
        if total_price:
            payment.total_price = total_price
        payment.save()

        serializer = PaymentSerializer(payment)

        return Response(serializer.data, status=status.HTTP_200_OK)
