from django.shortcuts import get_object_or_404, redirect, render
from django .contrib.auth.decorators import login_required

import doctors
from doctors.models import Doctor
import patients
from patients.models import Patient
from  .models import Appointments
# Create your views here.

@login_required
def appointments_list(request):
    appointments = Appointments.objects.all()
    return render(request, 'app_list.html',{'appointments': appointments})

@login_required
def appointments_create(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    if request.method =="POST":
     
        date= request.POST.get('date')
        time= request.POST.get('time')
        status= request.POST.get('status')
        specialization= request.POST.get('specialization')
        print(request.POST)
        print(request.POST.get('doctor'))

        Appointments.objects.create(

            patient_id = request.POST.get('patient'),
            doctor = Doctor.objects.get(id=request.POST.get('doctor')),
            appointments_time = f"{date} {time}",
            appointments_status="Scheduled",
            specialization=specialization,
            
            )
        
        return redirect('/appointments')
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    return render(request,'app_create.html',
                  { 
                    'patients': patients,
                    'doctors': doctors
                   }
    )


@login_required
def appointments_edit(request, pk):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    
    appointment= get_object_or_404(Appointments, pk=pk)
    if request.method =='POST':
        appointment.appointments_time = (f"{request.POST.get('date')} {request.POST.get('time')}")
        appointment.specialization= request.POST.get('specialization')
        appointment.appointments_status = "Scheduled"
        appointment.doctor_id = request.POST.get('doctor')
        appointment.patient_id = request.POST.get('patient')
        appointment.save()
        return redirect('/appointments')
    return render(request, 'app_edit.html', 
                  {'appointment': appointment,
                  'doctors': doctors,
                  'patients': patients
                  }
                  )


@login_required
def appointments_delete(request ,pk):
    appointment =get_object_or_404(Appointments, pk=pk)
    appointment.delete()
    return redirect('/appointments')