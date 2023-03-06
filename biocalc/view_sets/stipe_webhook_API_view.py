from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import stripe

from biocalc.models import Payment, Order

class StripeWebhookAPIView(APIView):
    """
    Stripe webhook API view to handle checkout session completed and other events.
    """

    def post(self, request, format=None):
        payload = request.body
        endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret)
        except ValueError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.SignatureVerificationError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            customer_email = session['customer_details']['email']
            order_id = session['metadata']['order_id']

            print('Payment successfull')

            payment = get_object_or_404(Payment, order=order_id)
            payment.status = 'C'
            payment.save()

            order = get_object_or_404(Order, id=order_id)
            order.status = 'C'
            order.save()

            # TODO - Decrease product quantity

            # send_payment_success_email_task.delay(customer_email)

        # Can handle other events here.

        return Response(status=status.HTTP_200_OK)