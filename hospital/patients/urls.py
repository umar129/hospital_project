from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    # API endpoints
    path('api/patients/', views.PatientAPIView.as_view(), name='api_patient_list'),
    path('api/patients/<int:pk>/', views.PatientDetailAPIView.as_view(), name='api_patient_detail'),
    
    # HTML views
    path('', views.patient_list, name='patient_list'),
    path('create/', views.patient_create, name='patient_create'),
    path('<int:pk>/update/', views.patient_update, name='patient_update'),
    path('<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    path('<int:pk>/detail/', views.patient_detail, name='patient_detail'),
]
