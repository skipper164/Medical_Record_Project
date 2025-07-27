from datetime import datetime, timedelta

from appointment_class.Doctor import Doctor
from appointment_class.patient import Patient


class Appointment:
    def __init__(self, doctor: Doctor, patient: Patient, time: datetime, duration: timedelta):
        self.doctor = doctor
        self.patient = patient
        self.time = time
        self.duration = duration

    def __str__(self) ->str:
        return (f'Appointment: {self.patient} with {self.doctor} ' 
                f"on {self.time} for {self.duration}  " )
