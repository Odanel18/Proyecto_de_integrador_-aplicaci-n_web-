from django.urls import path
from .views import UserCreateView

urlpatterns= [
    path("api/v1/registrar/",UserCreateView.as_view(),name='register-name'),

]