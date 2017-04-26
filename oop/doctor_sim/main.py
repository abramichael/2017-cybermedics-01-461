from doctor import Doctor 
from patient import Patient

doc1 = Doctor("gynecologist","Shamsutdinova")
print str(doc1)
doc2 = Doctor("psychologist", "Sharafeeva")
print str(doc2)

pat1 = Patient(fio="Egorova", age=20, gender="F", blood_type=2, Rh="+")
print str(pat1)
pat2 = Patient("Butorin", 20, "M", 2)
print str(pat2)

doc1.collect_anamnesis(pat1)
doc2.collect_anamnesis(pat2)