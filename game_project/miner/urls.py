from django.urls import path
from miner import views

app_name = 'miner'

urlpatterns = [
    path('',views.index,name='index'),
]