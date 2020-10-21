from rest_framework import viewsets, permissions

from .serializers import *
from .models import *



class UserProfileSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('clientUser_id')
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class HealthAgreementProfileSet(viewsets.ModelViewSet):
    queryset = HealthAgreement.objects.all().order_by('date')
    serializer_class = HealthAgreementSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClinicProfileSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all().order_by('clinic_name')
    serializer_class = ClinicSerializer
    permission_classes = [permissions.IsAuthenticated]

class AgreementProfileSet(viewsets.ModelViewSet):
    queryset = Agreement.objects.all().order_by('date')
    serializer_class = AgreementSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClinicsFranchiseProfileSet(viewsets.ModelViewSet):
    queryset = ClinicsFranchise.objects.all().order_by('franchise_full_name')
    serializer_class = ClinicsFranchiseSerializer
    permission_classes = [permissions.IsAuthenticated]

class AnalysisProfileSet(viewsets.ModelViewSet):
    queryset = Analysis.objects.all().order_by('analysis_name')
    serializer_class = AnalysisSerializer
    permission_classes = [permissions.IsAuthenticated]

class DoctorProfileSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('full_name')
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]