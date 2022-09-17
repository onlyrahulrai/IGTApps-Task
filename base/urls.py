from django.urls import path 
from .views import (
    details,
    identity,
    recognize,
    register,
)

urlpatterns = [ 
    path("",register,name="register"),
    path("identity/",identity,name="identity"),
    path("recognize/",recognize,name="recognize"),
    path("details/",details,name="details"),
]