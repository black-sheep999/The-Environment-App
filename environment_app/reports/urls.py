from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_issue, name='home'),
    path('report/', views.report_issue, name='report_issue'),
    path('report/success/', views.report_success, name='report_success'),
]
