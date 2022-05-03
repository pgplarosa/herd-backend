from django.urls import path

from . import views

urlpatterns = [
    path('research-relevance/', views.get_research_relevance_table, name="research_relevance_table"),
    path('scope/', views.get_research_relevance_scope, name="research_relevance"),
    path('citations/', views.get_citations, name="research_relevance"),
    path('patents/', views.get_patents, name="patents_table"),
    path('patents/type-per-univ', views.get_patent_type_per_university, name='patent_type_per_university')
]