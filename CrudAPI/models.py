from django.db import models
from django.contrib.auth.models import User

#class ClientUser(models.Model):

#    user_name = models.CharField(max_length=64)
#    user_surname = models.CharField(max_length=64)
#    user_email = models.EmailField()
#    user_keyword = models.CharField(max_length=64)
#    user_ccdata = models.CharField(max_length=64)
#    user_hashPassword = models.CharField(max_length=256)
#
 #   def __str__(self):
 #       return self.user_name + " " + self.user_surname + " (" + self.user_email + ")"



class UserProfile(models.Model):
    address = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='profiles')
    clientUser = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return ""



class Clinic(models.Model):
    franchise_name = models.CharField(max_length=64)
    clinic_name = models.CharField(max_length=64)
    doctor_type = models.CharField(max_length=64)
    clinic_address = models.TextField()

    def __str__(self):
        return self.clinic_name + " " + self.doctor_type + " (" + self.clinic_address + ")"

class HealthAgreement(models.Model):
    date = models.DateField()
    address = models.TextField()
    status = models.TextField()
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    def __str__(self):
        return  "UserID: " + str(self.user) + " - ClinicID: " + str(self.clinic) + "(" + self.address + ")"

class Agreement(models.Model):
    date = models.DateField()
    info = models.BinaryField()
    status = models.CharField(max_length=64)
    user1 = models.ForeignKey(User, related_name='agreement_sent', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='agreement_received', on_delete=models.CASCADE)
    def __str__(self):
        return ""



class ClinicsFranchise(models.Model):
    #franchise_name = models.CharField(max_length=64, default="HOME")
    franchise_full_name = models.CharField(max_length=64, default="HOME")
    franchise_addr = models.CharField(max_length=120)
    phone = models.CharField(max_length=64)
    email = models.EmailField

    def __str__(self):
        return str(self.franchise_full_name) + " " + str(self.franchise_addr)

class Analysis(models.Model):
    analysis_name = models.CharField(max_length=64)
    analysis_franchise_name = models.CharField(max_length=64)
    analysis_contents = models.CharField(max_length=1024)
    amount = models.IntegerField
    isHomeVisit = models.BooleanField
    def __str__(self):
        return str(self.analysis_name) + " from " #+ str(self.analysis_franchise_name)


class Doctor(models.Model):
    full_name = models.CharField(max_length=128)
    speciality = models.CharField(max_length=64)
    clinics_name = models.CharField(max_length=64)
    doctor_email = models.EmailField
    experience_years = models.IntegerField
    isConsultingInMessenger = models.BooleanField
    isVideoConsulting = models.BooleanField

    def __str__(self):
        return ""
