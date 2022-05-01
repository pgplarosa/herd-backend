from django.urls import path

from . import views

urlpatterns = [
    path('research-relevance/', views.get_research_relevance_table, name="research_relevance_table")
]