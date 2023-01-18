from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from django.db import IntegrityError

from .models import Item
from .serializers.common import ItemSerializer

class ItemListView(APIView):

  def get(self, _request):
    items = Item.objects.all()
    serialized_items = ItemSerializer(items, many=True)
    return Response(serialized_items.data, status=status.HTTP_200_OK)

  def post(self, request):
        item_to_add = ItemSerializer(data=request.data)
        try:
            item_to_add.is_valid()
            item_to_add.save()
            return Response(item_to_add.data, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except AssertionError as e:
            return Response({ "detail": str(e) }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({ "detail": "Unprocessable Entity" }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ItemDetailView(APIView):

  def get_item(self, pk):
    try:
      return Item.objects.get(pk=pk)
    except Item.DoesNotExist:
      raise NotFound(detail="Can't find that item! Your young cousins must've taken them.")

  def get(self, _request, pk):
    try:
      item = Item.objects.get(pk=pk)
      serialized_item = ItemSerializer(item)
      return Response(serialized_item.data, status=status.HTTP_200_OK)
    except Item.DoesNotExist:
      raise NotFound(detail="Can't find that item! Your young cousins must've lost them.")

  def put(self, request, pk):
    item_to_edit = self.get_item(pk=pk)
    updated_item = ItemSerializer(item_to_edit, data=request.data)
    try:
      updated_item.is_valid()
      updated_item.save()
      return Response(updated_item.data, status=status.HTTP_202_ACCEPTED)

    except AssertionError as e:
      return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except:
      res = {"detail": "Unprocessable Entity"}
      return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

  def delete(self, _request, pk):
    item_to_delete = self.get_item(pk=pk)
    item_to_delete.delete()
    return Response({"detail": "Deleted."}, status=status.HTTP_204_NO_CONTENT)