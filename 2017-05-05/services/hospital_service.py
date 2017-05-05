from repositories.doctor_repository import DoctorRepository

class HospitalService:

	def addPatientToDoctor(self, doctor, patient):
		d = DoctorRepository()
		lst = d.get_patients_of_doctor_by_doctor_name(doctor)
		if len(lst) == 3:
			print "sorry, no place for now"
		else:
			d.add_patient(doctor, patient)