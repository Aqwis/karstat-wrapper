from collections import defaultdict

class CourseResults:
	def __init__(self, course_code, course_name, from_year_semester, to_year_semester):
		self.course_code = course_code
		self.course_name = course_name
		self.from_year_semester = from_year_semester
		self.to_year_semester = to_year_semester

		self.grades = defaultdict(dict)
		self.number_of_candidates = None
		self.number_of_candidates_appearing = None
		self.number_of_passes = None
		self.number_of_failures = None
		self.number_of_withdrawals = None
		self.number_of_medical_certificates = None
		self.number_of_withdrawals_before_exam = None

	def set_grades_by_letter(self, letter, count):
		# The arguments should be tuples on the form (men, women).
		# Totals should be calculated from the pair of numbers.
		self.grades[letter] = count

	def set_basic_information(self, number_of_candidates, number_of_candidates_appearing, number_of_passes, number_of_failures, number_of_withdrawals, number_of_medical_certificates, number_of_withdrawals_before_exam):
		# Add number of failures, candidates, etc.
		# The arguments should be tuples on the form (men, women).
		# Totals should be calculated from the pair of numbers.
		self.number_of_candidates = number_of_candidates
		self.number_of_candidates_appearing = number_of_candidates_appearing
		self.number_of_passes = number_of_passes
		self.number_of_failures = number_of_failures
		self.number_of_withdrawals = number_of_withdrawals
		self.number_of_medical_certificates = number_of_medical_certificates
		self.number_of_withdrawals_before_exam = number_of_withdrawals_before_exam

	def validate(self):
		# TODO
		# Check if numbers add up
		return True

	def to_dict(self):
		# TODO
		# Converts object to dictionary
		return {
			"code": self.course_code,
			"name": self.course_name,
			"OSV": "OSV"
		}