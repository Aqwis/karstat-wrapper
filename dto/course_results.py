from collections import defaultdict

class CourseResults:
	def __init__(self, course_code, course_name, from_year_semester, to_year_semester):
		self.course_code = course_code
		self.course_name = course_name
		self.from_year_semester = from_year_semester
		self.to_year_semester = to_year_semester

		self.grades = defaultdict(dict)
		self.number_of_candidates = None
		self.number_stood_for_exam = None
		self.number_passed = None
		self.number_failed = None
		self.number_aborted = None
		self.number_doctors_note = None
		self.number_aborted_before_exam = None

	def set_grades_by_letter(self, letter, count):
		# The arguments should be tuples on the form (men, women).
		# Totals should be calculated from the pair of numbers.
		self.grades[letter] = count

	def set_basic_information(self, number_of_candidates, number_stood_for_exam, number_passed, number_failed, number_aborted, number_doctors_note, number_aborted_before_exam):
		# Add number of failures, candidates, etc.
		# The arguments should be tuples on the form (men, women).
		# Totals should be calculated from the pair of numbers.
		self.number_of_candidates = number_of_candidates
		self.number_stood_for_exam = number_stood_for_exam
		self.number_passed = number_passed
		self.number_failed = number_failed
		self.number_aborted = number_aborted
		self.number_doctors_note = number_doctors_note
		self.number_aborted_before_exam = number_aborted_before_exam

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