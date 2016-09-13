from datetime.datetime import now

from flask import jsonify, Blueprint

from dto.semester import YearSemester
from scraping.handlers.course_results_page import get_course_results

course_blueprint = Blueprint('course', __name__)

@course_blueprint.route('/course/<parameter_course_code>')
def course(parameter_course_code):
	course_code = parameter_code.upper()

	current_year = now.year
	current_season = 'VÅR' if now.month < 8 else 'HØST'
	default_year_semester = YearSemester(current_year, current_season)

	course_results = get_course_results(course_code, default_year_semester, default_year_semester)
	return jsonify(**course_results.to_dict())