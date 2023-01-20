from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import RedPackets
from .serializers.common import RedPacketSerializer
from .serializers.populated import PopulatedRedPacketSerializer

class RedPacketListView(APIView):

  # permission_classes = (IsAuthenticatedOrReadOnly, )

  def get(self, _request):
    redpackets = RedPackets.objects.all()
    serialized_redpackets = RedPacketSerializer(redpackets, many=True)
    return Response(serialized_redpackets.data, status=status.HTTP_200_OK)


  def post(self, request):
    request.data['owner'] = request.user.id
    redpackets_to_add = RedPacketSerializer(data=request.data)
    try:
      redpackets_to_add.is_valid()
      redpackets_to_add.save()
      return Response(redpackets_to_add.data, status=status.HTTP_201_CREATED)

    except IntegrityError as e:
      res = {
        "detail": str(e)
      }
      return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except AssertionError as e:
      return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except:
      return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class RedPacketDetailView(APIView):

  def get_redpackets(self, pk):
    try:
      return RedPackets.objects.get(pk=pk)
    except RedPackets.DoesNotExist:
      raise NotFound(detail="Can't find those red packets! You might have dropped them somewhere.")

  def get(self, _request, pk):
    try:
      redpackets = self.get_redpackets(pk=pk)
      serialized_redpackets = PopulatedRedPacketSerializer(redpackets)
      return Response(serialized_redpackets.data, status=status.HTTP_200_OK)
    except RedPackets.DoesNotExist:
      raise NotFound(detail="Can't find those red packets! You might have dropped them somewhere. 2")

  def put(self, request, pk):
    redpackets_to_update = self.get_redpackets(pk=pk)
    request.data['owner'] = request.user.id
    updated_redpackets = RedPacketSerializer(redpackets_to_update, data=request.data)
    try:
      updated_redpackets.is_valid()
      print(updated_redpackets.errors)
      updated_redpackets.save()
      return Response(updated_redpackets.data, status=status.HTTP_202_ACCEPTED)

    except AssertionError as e:
      return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except:
      res = {"detail": "Unprocessable Entity"}
      return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
