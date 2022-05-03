from django.shortcuts import render

from core.research_cost import get_research_cost_table as research_cost_table
from core.research_cost import get_research_cost_budget
from core.research_cost import get_research_cost_funding_type as funding_type
from core.research_cost import get_research_cost_funding_source as funding_source
from core.research_cost import get_research_cost_budget_line as funding_forecast
from core.utilities import makeJsonResponse, get_columns, process_for_response

from django.http import JsonResponse

def get_research_cost(request):
    data = research_cost_table()
    metadata = {
        "columns": get_columns(data)
    }
    return makeJsonResponse(data, metadata, is_modified=True)

# chart data

def get_research_funding(request):
    return makeJsonResponse(get_research_cost_budget())

def get_research_funding_type(request):
    return makeJsonResponse(funding_type())

def get_research_funding_source(request):
    return makeJsonResponse(funding_source())

def get_research_funding_forecast(request):
    return makeJsonResponse(funding_forecast())