import datetime

class Hospital:

	def __init__(self, name, address):
		self.name = name
		self.address = address
		self.analysis_schedule = {}
		self.begin_work = datetime.time(hour=8)
		self.end_work = datetime.time(hour=9)

	def get_available_day(self):
		dt = datetime.datetime.today()
		one_day = datetime.timedelta(days=1)
		available = False
		while (not available):
			str_dt = "%s.%s.%s" % (dt.day, dt.month, dt.year)
			if str_dt not in self.analysis_schedule:
				return dt
			else:
				day_schedule = self.analysis_schedule[str_dt]
				if (len(day_schedule) < 4):
					return dt
				else:
					dt += one_day

	def addToAnalysisSchedule(self, analysis):
		str_dt = "%s.%s.%s" % (analysis.date_time.day, 
			analysis.date_time.month, analysis.date_time.year)
		if str_dt not in self.analysis_schedule:
			self.analysis_schedule[str_dt] = []
		self.analysis_schedule[str_dt].append(analysis)
		print self.analysis_schedule



