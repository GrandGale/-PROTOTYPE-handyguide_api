from django.shortcuts import render
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from handouts.pagination import LimitOffsetPagination, get_paginated_response
from handouts.selectors import get_faculty_department_course_list, handouts_list
from handouts.utils import inline_serializer


# -------------------
# API Views
# -------------------


class FacultyDepartmentCourseListApi(APIView):
    """
    API view to retrieve lists of all faculties, departments, and courses."""

    class FacultySerializer(serializers.Serializer):
        name = serializers.CharField()
        abbrev = serializers.CharField()

    class DepartmentSerializer(serializers.Serializer):
        name = serializers.CharField()
        abbrev = serializers.CharField()

    class CourseSerializer(serializers.Serializer):
        name = serializers.CharField()
        code = serializers.CharField()

    def get(self, request):
        faculties, departments, courses = get_faculty_department_course_list()

        faculties_serializer = self.FacultySerializer(faculties, many=True)
        departments_serializer = self.DepartmentSerializer(departments, many=True)
        courses_serializer = self.CourseSerializer(courses, many=True)

        return Response(
            {
                "faculties": faculties_serializer.data,
                "departments": departments_serializer.data,
                "courses": courses_serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class HandoutsListApi(APIView):
    """
    API view to retrieve a list of handouts with optional filtering and pagination.
    """

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
        session = serializers.CharField()
        file_url = serializers.SerializerMethodField()

        def get_file_url(self, instance):
            return instance.file.url

    class FilterSerializer(serializers.Serializer):
        limit = serializers.IntegerField(required=False)
        offset = serializers.IntegerField(required=False)
        course_code = serializers.CharField(required=False)
        department = serializers.CharField(required=False)
        faculty = serializers.CharField(required=False)

    class Pagination(LimitOffsetPagination):
        default_limit = 10

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
