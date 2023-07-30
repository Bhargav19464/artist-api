from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer

class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class ArtistWorkListView(generics.ListAPIView):
    serializer_class = WorkSerializer

    def get_queryset(self):
        artist_name = self.kwargs['artist_name']
        return Work.objects.filter(artist__name__icontains=artist_name)

class WorkFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        work_type = request.query_params.get('work_type')
        if work_type:
            return queryset.filter(work_type=work_type)
        return queryset

class WorkListFilteredView(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [DjangoFilterBackend, WorkFilterBackend]
    filterset_fields = ['work_type']

class ArtistCreateView(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
