class ReportFormData:
	def __init__(self, course_code, from_year_semester, to_year_semester):
		self.course_code = course_code
		self.from_year_semester = from_year_semester
		self.to_year_semester = to_year_semester

	def _is_valid(self):
		return any(list(self.course_code).map(lambda a: a.isalpha()))
					and any(list(self.course_code).map(lambda a: a.isdigit()))
					and (1900 < self.from_year_semester.year < 2100)
					and (1900 < self.to_year_semester.year < 2100)
					and (self.from_year_semester.semester in ('VÅR', 'HØST',))
					and (self.to_year_semester.semester in ('VÅR', 'HØST',))

	def get_valid_dictionary(self):
		if !self._is_valid():
			raise Exception("Invalid data in object")
		return {
			"showWomen": "1",
			"singleOrPeriode": "P",
			"courseName": self.course_code,
			"versionCode": "1",
			"fromYear": str(self.from_year_semester.year),
			"toYear": str(self.to_year_semester.year),
			"fromSemester": self.from_year_semester.semester,
			"toSemester": self.to_year_semester.semester,
		}