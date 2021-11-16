from django.urls import path
from .views import DataView


app_name = 'core'

urlpatterns = [
    path('', DataView.as_view(), name='data'),
]
