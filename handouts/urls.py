from django.urls import path

from handouts.apis import FacultyDepartmentCourseLevelListApi, HandoutsListApi

urlpatterns = [
    path("data/", FacultyDepartmentCourseLevelListApi.as_view(), name="handouts-list"),
    path("handouts/", HandoutsListApi.as_view(), name="all-handouts"),
]
