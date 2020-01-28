from django.urls import path
from api import views

urlpatterns = [
        path('', views.GetConn.as_view(), name = 'test-conn'),

]
