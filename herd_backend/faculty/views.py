from django.shortcuts import render

from core.faculty import get_faculty_profile_table as faculty_profile
from core.faculty import get_faculty_educ_attain

from core.utilities import makeJsonResponse, get_columns

######################################
#      FACULTY PROFILE               #
######################################

def get_faculty_profile(request):
    data = faculty_profile()
    metadata = {
        "columns": get_columns(data)
    }
    return makeJsonResponse(data, metadata, is_modified=True)

# charts

def get_faculty_education(request):
    return makeJsonResponse(get_faculty_educ_attain())