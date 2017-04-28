from analysis import Analysis

class Doctor:
	def __init__(self, sp, fio):
		self.sp = sp
		self.fio = fio
		print "Doctor created."

	def __str__(self):
		return "%s %s"  % (self.sp, self.fio)

	def collect_anamnesis(self, patient):
		print "%s collected anamnesis from %s." % \
			(self, patient)

	def sendForAnalysis(self, pat1, hosp1, type_analysis):
		dt = hosp1.get_available_day()
		print dt
		a = Analysis(self, pat1, hosp1, type_analysis, dt)
		print str(a)
		return a