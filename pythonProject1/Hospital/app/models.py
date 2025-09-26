from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_Name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.patient_Name

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    dob = models.DateField()  # Date of Birth
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()  # Experience in years
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)  # Adjust length as needed
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ])
    address = models.TextField()
    file = models.FileField(upload_to='doctor_files/', blank=True, null=True)

    def __str__(self):
        return self.doctor_name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    