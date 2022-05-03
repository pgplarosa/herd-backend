from django.shortcuts import render

from core.research_cost import get_research_cost_table as research_cost_table
from core.research_cost import get_research_cost_budget
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
