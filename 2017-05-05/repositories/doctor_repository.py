class DoctorRepository:

	def get_patients_of_doctor_by_doctor_name(self, doctor):
		f = open("doctor_%s.txt" % doctor)
		lst = []
		for line in f:
			lst.append(line.strip())
		f.close()
		return lst


	def add_patient(self, doctor, patient):
		f = open("doctor_%s.txt" % doctor, "a")
		f.write("\n")
		f.write(patient)
		f.close()