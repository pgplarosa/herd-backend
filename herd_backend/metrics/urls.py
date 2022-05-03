from django.urls import path

from . import views

urlpatterns = [
    path('research-cost/', views.get_research_cost, name="research_cost"),
    path('research-cost/funding', views.get_research_funding, name='research_funding'),
    path('research-cost/funding-type', views.get_research_funding_type, name='research_funding_type'),
    path('research-cost/funding-source', views.get_research_funding_source, name="research_funding_source"),
    path('research-cost/funding-forecast', views.get_research_funding_forecast, name="research_funding_forecast")
]