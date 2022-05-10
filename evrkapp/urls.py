from django.urls import path
from django.shortcuts import redirect
import evrkapp.views as views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', lambda request: redirect('q1/', permanent=True)),
    path('q1/',views.last48hoursData,name='q1'),
    path('q2/',views.binOperations,name='q2'),
    ]