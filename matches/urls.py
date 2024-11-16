from django.urls import path
from .views import MatchListView, NewsListView

urlpatterns = [
    path('matches/', MatchListView.as_view(), name='match_list'),
    path('news/', NewsListView.as_view(), name='news_list'),
]
