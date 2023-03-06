from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import stripe

from biocalc.permissions import IsPaymentForOrderNotCompleted, DoesOrderHaveAddress
from biocalc.models import Order



class StripeCheckoutSessionCreateAPIView(APIView):
    """
    Create and return checkout session ID for order payment of type 'Stripe'
    """
    permission_classes = (IsPaymentForOrderNotCompleted,
                          DoesOrderHaveAddress, )

    def post(self, request, *args, **kwargs):
        order = get_object_or_404(Order, id=self.kwargs.get('order_id'))

        order_items = []

        for order_item in order.order_items.all():
            product = order_item.product
            quantity = order_item.quantity

            data = {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount_decimal': product.price,
                    'product_data': {
                        'name': product.name,
                        'description': product.desc,
                        'images': [f'{settings.BACKEND_DOMAIN}{product.image.url}']
                    }
                },
                'quantity': quantity
            }

            order_items.append(data)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=order_items,
            metadata={
                "order_id": order.id
            },
            mode='payment',
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL
        )

        return Response({'sessionId': checkout_session['id']}, status=status.HTTP_201_CREATED)
