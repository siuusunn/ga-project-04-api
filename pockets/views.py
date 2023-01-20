from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Pocket
from .serializers.common import PocketSerializer
from .serializers.populated import PopulatedPocketSerializer

class PocketListView(APIView):

  # permission_classes = (IsAuthenticatedOrReadOnly, )

  def get(self, _request):
    pocket = Pocket.objects.all()
    serialized_pocket = PocketSerializer(pocket, many=True)
    return Response(serialized_pocket.data, status=status.HTTP_200_OK)


  def post(self, request):
    request.data['owner'] = request.user.id
    pocket_to_add = PocketSerializer(data=request.data)
    try:
      pocket_to_add.is_valid()
      print(pocket_to_add.errors)
      pocket_to_add.save()
      return Response(pocket_to_add.data, status=status.HTTP_201_CREATED)

    except IntegrityError as e:
      res = {
        "detail": str(e)
      }
      return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except AssertionError as e:
      return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except:
      return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class PocketDetailView(APIView):

  def get_poket(self, pk):
    try:
      return Pocket.objects.get(pk=pk)
    except Pocket.DoesNotExist:
      raise NotFound(detail="Can't find those red packets! You might have dropped them somewhere.")

  def get(self, _request, pk):
    try:
      pocket = self.get_poket(pk=pk)
      serialized_pocket = PopulatedPocketSerializer(pocket)
      return Response(serialized_pocket.data, status=status.HTTP_200_OK)
    except Pocket.DoesNotExist:
      raise NotFound(detail="Can't find those red packets! You might have dropped them somewhere. 2")

  def put(self, request, pk):
    pocket_to_update = self.get_poket(pk=pk)
    request.data['owner'] = request.user.id
    updated_pocket = PocketSerializer(pocket_to_update, data=request.data)
    try:
      updated_pocket.is_valid()
      print(updated_pocket.errors)
      updated_pocket.save()
      return Response(updated_pocket.data, status=status.HTTP_202_ACCEPTED)

    except AssertionError as e:
      return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except:
      res = {"detail": "Unprocessable Entity"}
      return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
