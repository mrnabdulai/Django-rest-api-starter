from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class Orders():
    @staticmethod
    @api_view()
    def listOrders(request):
        return Response({'message': 'list of orders'}, 200)


@api_view(['POST', 'GET'])
def books(request):
    return Response("list of books", status=status.HTTP_200_OK)


# class BookView(views.APIView):
#     def get(self, request, pk):
#         return Response({"message": "single book with id " + str(pk)}, status.HTTP_200_OK)

#     def put(self, request, pk):
#         return Response({"title": request.data.get('title')}, status.HTTP_200_OK)


class BookView(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "All books"}, status.HTTP_200_OK)

    def create(self, request):
        return Response({"message": "Creating a book"}, status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        return Response({"message": "Updating a book"}, status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        return Response({"message": "Displaying a book"}, status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        return Response({"message": "Partially updating a book"}, status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        return Response({"message": "Deleting a book"}, status.HTTP_200_OK)


class MenuItemView(generics.ListCreateAPIView):
    pass


class ReadOnlyMenuItemView (viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
