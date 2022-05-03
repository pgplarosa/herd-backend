from django.urls import path

from . import views

urlpatterns = [
    path('profiles/', views.get_faculty_profile, name="faculty_profile"),
    path('profiles/education', views.get_faculty_education, name="faculty_education"),
]