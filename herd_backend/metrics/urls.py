from django.urls import path

from . import views

urlpatterns = [
    path('research-cost/', views.get_research_cost, name="research_cost"),
    path('research-cost/funding', views.get_research_funding, name='research_funding'),
    
]