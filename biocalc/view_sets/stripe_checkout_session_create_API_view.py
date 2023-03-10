from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import stripe

from biocalc.permissions import IsPaymentForOrderNotCompleted, DoesOrderHaveAddress
from biocalc.models import Order, ItemSellingData



class StripeCheckoutSessionCreateAPIView(APIView):
    """
    Create and return checkout session ID for order payment of type 'Stripe'
    """
    permission_classes = (
        IsPaymentForOrderNotCompleted,
        # DoesOrderHaveAddress,
        )

    def post(self, request, *args, **kwargs):
        order = get_object_or_404(Order, id=self.kwargs.get('order_id'))

        order_items = []

        for order_item in order.order_items.all():
            product = order_item.product
            itemData = ItemSellingData.objects.get(shop_item=product)
            quantity = order_item.quantity
            discount = 0
            q_discount = itemData.get_quantity_discount()
            if q_discount and q_discount['quantity'] <= quantity:
                discount = q_discount['discount']
            sale = itemData.get_sale_discount()
            if sale:
                discount = discount + sale
            if discount:
                price = itemData.get_price() - ((itemData.get_price() * discount) // 100)
            else: 
                price = itemData.get_price()

            data = {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount_decimal': price,
                    'product_data': {
                        'name': product.name
                    }
                },
                'quantity': quantity
            }
            print("stripe_checkout_session_create_API_view \n",q_discount, sale, itemData.get_price()," data: \n", data)
            order_items.append(data)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=order_items,
            metadata={
                "order_id": order.id
            },
            mode='payment',
            success_url=settings.SITE_URL + "/ty/?successful=true&session_id={CHECKOUT_SESSION_ID}",
            cancel_url=settings.SITE_URL + "/?canceled=true",
        )
        print("stripe_checkout_session_create_API_view \n checkout_session: \n", checkout_session)

        return Response({'sessionId': checkout_session['id'], "url":checkout_session['url']}, status=status.HTTP_201_CREATED)
