from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Comment
from .serializers.common import CommentSerializer
# from .serializers.populated import PopulatedcommentSerializer

class CommentListView(APIView):

  # permission_classes = (IsAuthenticatedOrReadOnly, )

  def get(self, _request):
    comments = Comment.objects.all()
    serialized_comments = CommentSerializer(comments, many=True)
    return Response(serialized_comments.data, status=status.HTTP_200_OK)

  def post(self, request):
        comment_to_add = CommentSerializer(data=request.data)
        try:
            comment_to_add.is_valid()
            comment_to_add.save()
            return Response(comment_to_add.data, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except AssertionError as e:
            return Response({ "detail": str(e) }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({ "detail": "Unprocessable Entity" }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class CommentDetailView(APIView):

  def get_comment(self, pk):
    try:
      return Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
      raise NotFound(detail="Can't find that comment! Your young cousins must've taken them.")

  def get(self, _request, pk):
    try:
      comment = self.get_comment(pk=pk)
      serialized_comment = CommentSerializer(comment)
      return Response(serialized_comment.data, status=status.HTTP_200_OK)
    except comment.DoesNotExist:
      raise NotFound(detail="Can't find that comment! Your young cousins must've lost them.")

  def put(self, request, pk):
    comment_to_edit = self.get_comment(pk=pk)
    updated_comment = CommentSerializer(comment_to_edit, data=request.data)
    try:
      updated_comment.is_valid()
      updated_comment.save()
      return Response(updated_comment.data, status=status.HTTP_202_ACCEPTED)

    except AssertionError as e:
      return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except:
      res = {"detail": "Unprocessable Entity"}
      return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

  def delete(self, _request, pk):
    comment_to_delete = self.get_comment(pk=pk)
    comment_to_delete.delete()
    return Response({"detail": "Deleted."}, status=status.HTTP_204_NO_CONTENT)