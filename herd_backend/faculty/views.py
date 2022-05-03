from django.shortcuts import render
from django.http import JsonResponse

from core.faculty import get_faculty_profile_table as faculty_profile
from core.faculty import get_faculty_educ_attain

from core.utilities import makeJsonResponse, get_columns, invert_table, \
        create_stacked_bar_chart_data

######################################
#      FACULTY PROFILE               #
######################################

def get_faculty_profile(request):
    return JsonResponse(invert_table(faculty_profile()), safe=False)
    
# charts

def get_faculty_education(request):
    return JsonResponse(create_stacked_bar_chart_data(get_faculty_educ_attain()), safe=False)
