from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_csv.renderers import CSVRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, throttle_classes
from rest_framework import viewsets
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework_yaml.renderers import YAMLRenderer
from .serializers import MenuSerializer, CategorySerializer
from .models import Menu, Category
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage

import bleach
# Create your views here.


class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    ordering_fields = ['price', 'inventory']
    search_fields = ['title', 'category__title']


@api_view(['GET', 'POST'])
# @renderer_classes([YAMLRenderer])
def menu_items(request):
    if request.method == 'GET':
        category_name = request.query_params.get("category")
        to_price = request.query_params.get("to_price")
        ordering = request.query_params.get('ordering')
        print(category_name)
        print(to_price)
        items = Menu.objects.select_related('category').all()
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)
        page = request.query_params.get('page', default=1)
        per_page = request.query_params.get("per_page", default=2)

        pagination = Paginator(items, per_page=per_page)
        try:
            items = pagination.page(number=page)

        except EmptyPage:
            items = []
        serialized_item = MenuSerializer(
            items, many=True, context={'request': request})

        # data = '<html><body><h1>Welcome To Little Lemon API Project</h1></body></html>'
        return Response(serialized_item.data)

    if request.method == 'POST':
        serialized_item = MenuSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        # can only be accessed after calling save method
        return Response(serialized_item.data)


@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)


@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "This is the endpoint message"})


@api_view()
@permission_classes([IsAuthenticated])
def manager(request):
    if request.user.groups.filter(name="Manager").exists():
        return Response({"message": "Only the manager can see this"})
    else:
        return Response({"message": "This is not meant for you to see"}, 403)


@api_view()
@throttle_classes([UserRateThrottle])
def throttle(request):
    return Response({"message": "This endpoint has throthling enabled"})
