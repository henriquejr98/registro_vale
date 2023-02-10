from django.contrib import admin
from django.urls import path
from . import views

app_name = 'registro'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:employee_id>/detalhes/', views.detail_by_employee, name='detail_by_employee'),
    path('<str:month>/detalhes/', views.detail_by_month, name='detail_month'),
    path('<int:employee_id>/novo_vale/', views.new_loan, name='new_loan'),
]
