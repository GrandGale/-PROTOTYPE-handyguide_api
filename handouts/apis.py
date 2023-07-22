from django.shortcuts import render
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from handouts.pagination import LimitOffsetPagination, get_paginated_response
from handouts.selectors import handouts_list

from handouts.utils import inline_serializer


class HandoutsListApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 1

    class FilterSerializer(serializers.Serializer):
        limit = serializers.IntegerField()
        offset = serializers.IntegerField(required=False)

    class OutputSerializer(serializers.Serializer):
        course = inline_serializer(
            fields={
                "name": serializers.CharField(),
                "code": serializers.CharField(),
            }
        )
        department = inline_serializer(
            fields={
                "name": serializers.CharField(),
                "abbrev": serializers.CharField(),
            }
        )
        faculty = inline_serializer(
            fields={
                "name": serializers.CharField(),
                "abbrev": serializers.CharField(),
            }
        )
        session = inline_serializer(fields={"name": serializers.CharField()})
        file_url = serializers.SerializerMethodField()

        def get_file_url(self, instance):
            return instance.file.url

    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        handouts = handouts_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=handouts,
            request=request,
            view=self,
        )
