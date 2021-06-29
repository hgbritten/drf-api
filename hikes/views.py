from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import HikeSerializer
from .models import Hike


class HikeList(ListCreateAPIView):
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer


class HikeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer
