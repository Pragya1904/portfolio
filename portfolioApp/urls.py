from django.urls import path
from . import views


urlpatterns =[
    path("",views.portfolio_index,name="portfolio_index"),
]