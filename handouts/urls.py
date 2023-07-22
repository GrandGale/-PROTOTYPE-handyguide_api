from django.urls import path

from handouts.apis import HandoutsListApi

urlpatterns = [
    path("", HandoutsListApi.as_view(), name="all-handouts"),
    # path("filter/", GetFilteredHandoutsApi.as_view(), name="filtered-handouts"),
    
]
