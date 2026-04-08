from django.db import models

# Create your models here.
class Appointments(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE)
    appointments_time = models.DateTimeField()
    appointments_field = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient} - {self.doctor}"