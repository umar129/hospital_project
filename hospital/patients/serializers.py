from rest_framework import serializers
from .models import Patients
from doctors.models import Doctors


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['id', 'name', 'department']


class PatientSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctors.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Patients
        fields = ['id', 'name', 'age', 'address', 'mobile', 'email', 'doctor', 'doctor_id']

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError("Age must be greater than 0.")
        if value > 150:
            raise serializers.ValidationError("Age must be less than 150.")
        return value

    def validate_mobile(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("Mobile number must be 10 digits.")
        if not value.isdigit():
            raise serializers.ValidationError("Mobile number must contain only digits.")
        return value

    def validate_email(self, value):
        if '@' not in value or '.' not in value:
            raise serializers.ValidationError("Invalid email format.")
        return value

    def create(self, validated_data):
        doctor_id = validated_data.pop('doctor_id', None)
        patient = Patients.objects.create(**validated_data)
        if doctor_id:
            patient.doctor = doctor_id
            patient.save()
        return patient
