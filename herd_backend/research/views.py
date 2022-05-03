from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
from core.research_relevance import get_research_relevance_table as research_relevance_table
from core.research_relevance import get_research_relevance_scope as research_relevance
from core.research_relevance import get_research_relevance_citations as citations
from core.patent import get_patent_table as patents_table

from core.utilities import process_for_response, get_columns


def get_research_relevance_table(request):
    data = research_relevance_table()
    metadata = {
        "columns": get_columns(data)
    }
    return JsonResponse(process_for_response(data, metadata), safe=False)

def get_research_relevance_scope(request):
    return JsonResponse(research_relevance(), safe=False)

def get_citations(request):
    return JsonResponse(citations(), safe=False)

def get_patents(request):
    data = patents_table()
    metadata = {
        "columns": get_columns(data)
    }
    return JsonResponse(process_for_response(data, metadata), safe=False)
