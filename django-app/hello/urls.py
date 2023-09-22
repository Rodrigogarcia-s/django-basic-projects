from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("rodrigo", views.rodrigo, name="rodrigo"),
    path("david", views.david, name="david")
]