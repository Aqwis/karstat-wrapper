import requests
from pyquery import PyQuery as pq

from dto.report_form_data import ReportFormData
from dto.course_results import CourseResults
from dto.semester import YearSemester
from scraping.handlers.feide_login import login

NUMBER_OF_CANDIDATES = 'Number of candidates (registered)'
NUMBER_OF_CANDIDATES_APPEARING = 'Candidates appearing at the examination'
NUMBER_OF_PASSES = 'Number of passes (B)'
NUMBER_OF_FAILURES = 'Number of failures (S)'
NUMBER_OF_WITHDRAWALS = 'Number of withdrawals during examination (A)'
FAILURES_AND_WITHDRAWALS = '\% failures and withdrawals'
MEAN_GRADE = 'Mean grade'
NUMBER_OF_MEDICAL_CERTIFICATES = 'Number presenting medical certificates (L)'
NUMBER_OF_WITHDRAWALS_BEFORE = 'Number of withdrawals before examination (T)'

def parse_course_results_page(html):
	# TODO
	# Parse the HTML of a retrieved course results page, and return
	# the information contained on the page.
	dom = pq(html)
	content_tables = dom('.questtop table td:last-of-type')

	# Grade counts
	pass_grade_names = ['A', 'B', 'C', 'D', 'E']
	pass_grade_counts = content_tables[-5:]
	pass_grades = dict(zip(pass_grade_names, pass_grade_counts))

	# Grade information
	information_names = [NUMBER_OF_CANDIDATES, CANDIDATES_APPEARING, NUMBER_OF_PASSES, NUMBER_OF_FAILURES, NUMBER_OF_WITHDRAWALS, MEAN_GRADE, NUMBER_OF_MEDICAL_CERTIFICATES, NUMBER_OF_WITHDRAWALS_BEFORE]
	information_counts = content_tables[0:5] + content_tables[6:9]
	information = dict(zip(information_names, information_counts))

	# Course code and name
	# Ugly selector
	basic_course_info_lines = dom('body > table:nth-child(3) > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr > td > table > tbody > tr > td > p:nth-child(8) > table > tbody > tr:nth-child(1) > td')[0].text().split('\n')
	course_code = basic_course_info_lines[3].strip()
	course_name = basic_course_info_lines[7].strip()

	# Year and semester
	select_values = [sel.value for sel in dom('select')]
	from_year_semester = YearSemester(select_values[0], select_values[1])
	to_year_semester = YearSemester(select_values[2], select_values[3])
	
	course_results = CourseResults(course_code, course_name, from_year_semester, to_year_semester)
	course_results.set_basic_information(information_counts)

def get_course_results_page(course_code, from_year_semester, to_year_semester, cookies=None):
	# Attempts to retrieve the grade statistics for a specific course between
	# two semesters.
	form_data = ReportFormData(course_code, from_year_semester, to_year_semester)
	response = requests.post('https://sats.itea.ntnu.no/karstat/makeReport.do', files=form_data.get_valid_dictionary(), cookies=cookies)
	return response.text

def is_page_course_results(html):
	# Checks whether a given page is in fact a course results page, or something
	# else. Does this by checking whether the HTML contains a known string.
	return "Antall kandidater i parentes" in html

def get_course_results(course_code, from_year_semester, to_year_semester):
	# Get the grade statistics for a specific course between two semesters
	html = get_course_results_page(course_code, from_year_semester, to_year_semester)
	if not is_page_course_results(html):
		success, cookies = login()
		html = get_course_results_page(course_code, from_year_semester, to_year_semester, cookies=cookies)
		print(html)

	if not is_page_course_results(html):
		raise Exception("Page was neither a course results page nor a FEIDE login page")

	return parse_course_results_page(html)