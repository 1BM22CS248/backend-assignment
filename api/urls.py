from django.urls import path
from . import views

urlpatterns = [
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('patients/', views.PatientListCreateView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('doctors/', views.DoctorListCreateView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('mappings/', views.MappingListCreateView.as_view(), name='mapping-list'),
    path('mappings/<int:pk>/', views.MappingDetailView.as_view(), name='mapping-detail'),
    path('mappings/patient/<int:patient_id>/', views.PatientMappingsView.as_view(), name='patient-mappings'),
]