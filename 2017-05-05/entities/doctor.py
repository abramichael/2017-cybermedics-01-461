class Doctor:
	def __init__(self, sp, fio):
		self.sp = sp
		self.fio = fio
		print "Doctor created."

	def __str__(self):
		return "%s %s"  % (self.sp, self.fio)