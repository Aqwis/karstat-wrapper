import requests

from dto.report_form_data import ReportFormData
from dto.course_results import CourseResults
from dto.semester import YearSemester
from scraping.handlers.feide_login import is_page_feide_login, login

def parse_course_results_page(html):
	# TODO
	# Parse the HTML of a retrieved course results page, and return
	# the information contained on the page.
	course_code = "DUMMY12345"
	course_name = "Dummy course"
	from_year_semester = YearSemester(2015, 'VÅR')
	to_year_semester = YearSemester(2016, 'HØST')
	
	course_results = CourseResults(course_code, course_name, from_year_semester, to_year_semester)
	return CourseResults()

def get_course_results_page(course_code, from_year_semester, to_year_semester):
	# Attempts to retrieve the grade statistics for a specific course between
	# two semesters.
	form_data = ReportFormData(course_code, from_year_semester, to_year_semester)
	response = requests.post('https://sats.itea.ntnu.no/karstat/makeReport.do', files=form_data.get_valid_dictionary())
	return response.text

def is_page_course_results(html):
	# Checks whether a given page is in fact a course results page, or something
	# else. Does this by checking whether the HTML contains a known string.
	return "Antall kandidater i parentes" in html

def get_course_results(course_code, from_year_semester, to_year_semester):
	# Get the grade statistics for a specific course between two semesters
	html = get_course_results_page(course_code, start_semester, end_semester)
	while not is_page_course_results(html):
		if is_page_feide_login(html):
			login()
			html = get_course_results_page(course_code, start_semester, end_semester)
		else:
			raise Exception("Page was neither a course results page nor a FEIDE login page")

	return parse_course_results_page(html)