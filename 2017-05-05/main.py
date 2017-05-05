from entities.doctor import Doctor
from entities.patient import Patient
from services.hospital_service import HospitalService

#doc = Doctor("psychologist", "Sharafeeva")
#pat = Patient(fio="Egorova", age=20, gender="F", blood_type=2, Rh="+")

doc_name = raw_input()
pat_name = raw_input()
h = HospitalService()
h.addPatientToDoctor(doc_name, pat_name)