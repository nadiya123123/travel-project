from . import views
from django.urls import path

urlpatterns = [
    path('', views.fun1, name='fun1')

]