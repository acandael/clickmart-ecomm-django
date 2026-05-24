from gc import get_objects

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cart, CartItem, Product
from .serializers import CartItemSerializer, CartSerializer


# Create your views here.
class CartListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        # if created:
        #     print('cart created')
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)

        if not product_id:
            return Response({"error": "product_id is required"}, status=400)

        product = get_object_or_404(Product, id=product_id, is_active=True)

        cart, _ = Cart.objects.get_or_create(user=request.user)

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            item.quantity += int(quantity)
            item.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ManageCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, item_id):
        if "change" not in request.data:
            return Response({"error": "change is required"}, status=400)

        change = int(request.data.get("change"))

        item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
        product = item.product

        if change > 0:
            if item.quantity + change > product.stock:
                return Response({"error": "Not enough stock"})

        new_qty = item.quantity + change

        if new_qty <= 0:
            item.delete()
            return Response({"success": "Item removed from cart"})

        item.quantity = new_qty
        item.save()
        serializer = CartItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, item_id):
        item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
        item.delete()
        return Response(
            {"success": "Item removed from cart"}, status=status.HTTP_204_NO_CONTENT
        )
