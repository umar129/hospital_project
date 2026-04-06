from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patients
from .serializers import PatientSerializer
from doctors.models import Doctors, Departments


# ===== API VIEWS =====
class PatientAPIView(APIView):
    """
    API to list all patients and create a new patient
    GET /api/patients/ - List all patients
    POST /api/patients/ - Create new patient
    """
    def get(self, request):
        patients = Patients.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Patient created successfully', 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDetailAPIView(APIView):
    """
    API to retrieve, update, or delete a specific patient
    """
    def get(self, request, pk):
        try:
            patient = Patients.objects.get(id=pk)
            serializer = PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Patients.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            patient = Patients.objects.get(id=pk)
            serializer = PatientSerializer(patient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {'message': 'Patient updated successfully', 'data': serializer.data},
                    status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Patients.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            patient = Patients.objects.get(id=pk)
            patient.delete()
            return Response({'message': 'Patient deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Patients.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)


# ===== HTML VIEWS =====
def patient_list(request):
    """Display list of all patients with their assigned doctors"""
    patients = Patients.objects.select_related('doctor').all()
    context = {
        'patients': patients,
        'total_patients': patients.count()
    }
    return render(request, 'patients/patient_list.html', context)


def patient_create(request):
    """Create a new patient"""
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('patients:patient_list')
        else:
            doctors = Doctors.objects.all()
            return render(request, 'patients/patient_form.html', {
                'errors': serializer.errors,
                'doctors': doctors,
                'form_data': request.POST
            })
    
    doctors = Doctors.objects.all()
    return render(request, 'patients/patient_form.html', {'doctors': doctors})


def patient_update(request, pk):
    """Update patient details"""
    patient = get_object_or_404(Patients, id=pk)
    
    if request.method == 'POST':
        serializer = PatientSerializer(patient, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('patients:patient_list')
        else:
            doctors = Doctors.objects.all()
            return render(request, 'patients/patient_form.html', {
                'errors': serializer.errors,
                'doctors': doctors,
                'patient': patient,
                'form_data': request.POST
            })
    
    doctors = Doctors.objects.all()
    return render(request, 'patients/patient_form.html', {
        'patient': patient,
        'doctors': doctors
    })


def patient_delete(request, pk):
    """Delete a patient"""
    patient = get_object_or_404(Patients, id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patients:patient_list')
    
    return render(request, 'patients/patient_confirm_delete.html', {'patient': patient})


def patient_detail(request, pk):
    """Display patient details"""
    patient = get_object_or_404(Patients, id=pk)
    return render(request, 'patients/patient_detail.html', {'patient': patient})

