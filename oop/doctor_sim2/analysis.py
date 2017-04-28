class Analysis:
	def __init__(self, doc, pat1, hosp1, type_analysis, dt):
		self.doctor = doc
		self.patient = pat1
		self.hospital = hosp1
		self.type_analysis = type_analysis
		self.date_time = dt
		self.made = False
		self.result = ""

		# hospital should know about analysis
		self.hospital.addToAnalysisSchedule(self)

	def __str__(self):
		return "Analysis %s for %s" % (self.type_analysis,
			self.patient)

	def __repr__(self):
		return "Analysis %s for %s" % (self.type_analysis,
			self.patient)