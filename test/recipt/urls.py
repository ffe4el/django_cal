from django.urls import path
from .views import get_recipt, get_budget

urlpatterns = [
    path('recipt', get_recipt),
    path('budget', get_budget),
    # path('budget_', get)



]