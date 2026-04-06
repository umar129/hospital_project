from rest_framework import serializers
from .models import Doctors, Departments


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id', 'dep_name']


class DoctorSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Departments.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Doctors
        fields = ['id', 'name', 'department', 'department_id', 'joining_date', 'salary']

    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError("Salary must be greater than 0.")
        return value

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Doctor name must be at least 3 characters long.")
        return value

    def create(self, validated_data):
        department_id = validated_data.pop('department_id', None)
        doctor = Doctors.objects.create(**validated_data)
        if department_id:
            doctor.department = department_id
            doctor.save()
        return doctor

    def update(self, instance, validated_data):
        department_id = validated_data.pop('department_id', None)
        instance.name = validated_data.get('name', instance.name)
        instance.salary = validated_data.get('salary', instance.salary)
        if department_id:
            instance.department = department_id
        instance.save()
        return instance
