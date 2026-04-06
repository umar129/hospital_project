from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctors, Departments
from .serializers import DoctorSerializer


# ===== API VIEWS =====
class DoctorAPIView(APIView):
    """
    API to list all doctors and create a new doctor
    GET /api/doctors/ - List all doctors
    POST /api/doctors/ - Create new doctor
    """
    def get(self, request):
        doctors = Doctors.objects.select_related('department').all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Doctor created successfully', 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorDetailAPIView(APIView):
    """
    API to retrieve, update, or delete a specific doctor
    """
    def get(self, request, pk):
        try:
            doctor = Doctors.objects.get(id=pk)
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Doctors.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            doctor = Doctors.objects.get(id=pk)
            serializer = DoctorSerializer(doctor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {'message': 'Doctor updated successfully', 'data': serializer.data},
                    status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Doctors.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            doctor = Doctors.objects.get(id=pk)
            doctor.delete()
            return Response({'message': 'Doctor deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Doctors.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)


# ===== HTML VIEWS =====
def doctor_list(request):
    """Display list of all doctors"""
    doctors = Doctors.objects.select_related('department').all()
    departments = Departments.objects.all()
    context = {
        'doctors': doctors,
        'departments': departments,
        'total_doctors': doctors.count()
    }
    return render(request, 'doctors/doctor_list.html', context)


def doctor_create(request):
    """Create a new doctor"""
    if request.method == 'POST':
        serializer = DoctorSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('doctors:doctor_list')
        else:
            departments = Departments.objects.all()
            return render(request, 'doctors/doctor_form.html', {
                'errors': serializer.errors,
                'departments': departments,
                'form_data': request.POST
            })
    
    departments = Departments.objects.all()
    return render(request, 'doctors/doctor_form.html', {'departments': departments})


def doctor_update(request, pk):
    """Update doctor details"""
    doctor = get_object_or_404(Doctors, id=pk)
    
    if request.method == 'POST':
        serializer = DoctorSerializer(doctor, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('doctors:doctor_list')
        else:
            departments = Departments.objects.all()
            return render(request, 'doctors/doctor_form.html', {
                'errors': serializer.errors,
                'departments': departments,
                'doctor': doctor,
                'form_data': request.POST
            })
    
    departments = Departments.objects.all()
    return render(request, 'doctors/doctor_form.html', {
        'doctor': doctor,
        'departments': departments
    })


def doctor_delete(request, pk):
    """Delete a doctor"""
    doctor = get_object_or_404(Doctors, id=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctors:doctor_list')
    
    return render(request, 'doctors/doctor_confirm_delete.html', {'doctor': doctor})


def doctor_detail(request, pk):
    """Display doctor details"""
    doctor = get_object_or_404(Doctors, id=pk)
    return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})
