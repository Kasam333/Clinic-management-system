from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('doctor-login/', views.doctor_login, name="doctor-login"),
    path('doctor-register/', views.doctor_register, name="doctor-register"),
    path('reset-password/', views.doctor_reset_password, name="reset-password"),
    path('doctor-logout/', views.doctor_logout, name="doctor-logout"),
    path('doctor-dashboard/', views.doctor_dashboard, name="doctor-dashboard"),
    path('quick-add-patient-form/', views.quick_add_patient, name="quick-add-patient"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('patients/', views.patient, name="all-patients"),
    path('add-patient-form/', views.add_patient, name="add-patient"),
    path('patients/update/<int:id>', views.update_patient, name="update-patient"),
    path('patients/delete/<int:id>', views.delete_patient, name="delete-patient"),

    #Reports
    path('reports/', views.reports, name="reports"),
    path('collection-report/', views.collection_reports, name="collection-report"),
]
