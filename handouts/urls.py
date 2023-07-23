from django.urls import path

from handouts.apis import FacultyDepartmentCourseListApi, HandoutsListApi

urlpatterns = [
    path("data/", FacultyDepartmentCourseListApi.as_view(), name="handouts-list"),
    path("handouts/", HandoutsListApi.as_view(), name="all-handouts"),
]
