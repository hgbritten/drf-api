from django.urls import path
from .views import HikeList, HikeDetail

urlpatterns = [
    path("", HikeList.as_view(), name="hike_list"),
    path("<int:pk>/", HikeDetail.as_view(), name="hike_detail"),
]
