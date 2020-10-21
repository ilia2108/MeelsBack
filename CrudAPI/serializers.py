#serializers.py

from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','clientUser', 'address', 'phone')

class HealthAgreementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HealthAgreement
        fields = ('id','date', 'address', 'status', 'price', 'user', 'clinic')

class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clinic
        fields = ('id','clinic_name', 'doctor_type', 'clinic_address')

class AgreementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agreement
        fields = ('id','date' 'info', 'status', 'user1', 'user2')

class ClinicsFranchiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClinicsFranchise
        fields = ('id', 'franchise_full_name', 'franchise_addr', 'phone', 'email')

class AnalysisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Analysis
        fields = ('id', 'analysis_name', 'analysis_franchise_name', 'analysis_contents', 'amount', 'isHomeVisit')

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'full_name', 'speciality', 'clinics_name', 'doctor_email', 'experience_years',
               'isConsultingInMessenger', 'isVideoConsulting')