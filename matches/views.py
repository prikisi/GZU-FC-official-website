from django.shortcuts import render
from django.views.generic import ListView
from .models import Match, News


class MatchListView(ListView):
    model = Match
    template_name = 'matches/match_list.html'
    context_object_name = 'matches'
    paginate_by = 9
    ordering = ['-date']
    

class NewsListView(ListView):
    model = News
    template_name = 'matches/news_list.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 9
    

