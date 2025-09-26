from django.shortcuts import render,redirect,get_object_or_404
from app.models import Patient,Doctor,Appointment


# def BASE(request):
#     patients = Patient.objects.all()  # Fetch all patients from the database
#     return render(request, 'base.html')
def BASE(request):
    return render(request, 'base.html')

def ALL_PATIENTS(request):
    patients = Patient.objects.all()  # Fetch all patients from the database
    return render(request, 'patients/all_patients.html', {'patients': patients})

def ABOUT_PATIENT(request):
    patient_id = 1  # Specify the patient ID directly
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'patients/about_patient.html', {'patient': patient})

def EDIT_PATIENT(request):
    if request.method == "POST":
        patient_id=1
        patient_id = request.POST.get('patient_id')  # Get the patient ID from the form
        patient = get_object_or_404(Patient, id=patient_id)
        
        # Update patient details
        patient.patient_Name = request.POST.get('patient_name')
        patient.date_of_birth = request.POST.get('dob')
        patient.age = request.POST.get('age')
        patient.phone = request.POST.get('phone')
        patient.email = request.POST.get('email')
        patient.gender = request.POST.get('gender')
        patient.address = request.POST.get('address')
        patient.save()
        return redirect('all_patients')  # Redirect after editing

    # If GET request, render the form without a specific patient ID
    return render(request, 'patients/edit_patient.html')

def ADD_PATIENT(request):
    if request.method == "POST":
        patient_name = request.POST.get('patient_name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        patient = Patient(
            patient_Name = patient_name,
            date_of_birth = dob ,
            age = age,
            phone = phone,
            email = email,
            address = address,
        )
        patient.save()
        
    return render(request,'patients/add_patient.html')


def ADD_DOCTOR(request):
    if request.method == "POST":
        # Get the data from the form
        doctor_name = request.POST.get('doctor_name')
        dob = request.POST.get('dob')
        specialization = request.POST.get('specialization')
        experience = request.POST.get('experience')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        file = request.FILES.get('file')

        # Create and save the doctor instance
        doctor = Doctor(
            doctor_name=doctor_name,
            dob=dob,
            specialization=specialization,
            experience=experience,
            age=age,
            phone=phone,
            email=email,
            gender=gender,
            address=address,
            file=file
        )
        doctor.save()
        

    return render(request, 'doctors/add_doctor.html')

def all_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/all_doctor.html', {'doctors': doctors})

def ABOUT_DOCTOR(request):
    doctor_id = 1  # Specify the doctor ID directly
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'doctors/about_doctor.html', {'doctor': doctor})


def EDIT_DOCTOR(request):
    if request.method == "POST":
        doctor_id = request.POST.get('doctor_id')  # Get the doctor ID from the form
        doctor = get_object_or_404(Doctor, id=doctor_id)
        
        # Update doctor details
        doctor.doctor_name = request.POST.get('doctor_name')
        doctor.date_of_birth = request.POST.get('dob')
        doctor.specialization = request.POST.get('specialization')
        doctor.experience = request.POST.get('experience')
        doctor.age = request.POST.get('age')
        doctor.phone = request.POST.get('phone')
        doctor.email = request.POST.get('email')
        doctor.gender = request.POST.get('gender')
        doctor.address = request.POST.get('address')
        doctor.save()
        return redirect('all_doctor')  # Redirect after editing

    # If GET request, render the form without a specific doctor ID
    return render(request, 'doctors/edit_doctor.html')

def add_appointment(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        patient_name = request.POST.get('patient_name')
        appointment_date = request.POST.get('appointment_date')
        reason = request.POST.get('reason')

        # Create and save the appointment
        Appointment.objects.create(
            doctor_id=doctor_id,
            patient_name=patient_name,
            appointment_date=appointment_date,
            reason=reason
        )
        return redirect('all_appointments')  # Redirect after saving

    doctors = Doctor.objects.all()  # Get all doctors for the dropdown
    return render(request, 'appointments/add_appointment.html', {'doctors': doctors})

def all_appointment(request):
    appointments = Appointment.objects.all()  # Fetch all appointments
    return render(request, 'appointments/all_appointment.html', {'appointment': appointments})