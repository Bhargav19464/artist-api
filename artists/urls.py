from django.urls import path
from .views import WorkListCreateView, WorkListFilteredView, ArtistWorkListView, ArtistCreateView

urlpatterns = [
    path('works/', WorkListCreateView.as_view(), name='work-list-create'),
    path('works/filter/', WorkListFilteredView.as_view(), name='work-list-filtered'),
    path('works/<str:artist_name>/', ArtistWorkListView.as_view(), name='artist-work-list'),
    path('register/', ArtistCreateView.as_view(), name='artist-register'),
]
