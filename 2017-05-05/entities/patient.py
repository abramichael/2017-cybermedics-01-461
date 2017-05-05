from helpers.helpers import convert_blood_type as conv

class Patient:
	def __init__ (self, fio, age, gender, blood_type=1, Rh="+"):
		self.fio = fio
		self.age = age
		self.gender = gender
		self.blood_type = blood_type
		self.Rh = Rh
		print "Patient created."

	def __str__(self):
		return "%s (%s%s)"  % (self.fio, conv(self.blood_type), self.Rh )
