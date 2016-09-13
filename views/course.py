from flask import jsonify, Blueprint

course_blueprint = Blueprint('course', __name__)

@course_blueprint.route('/course/<parameter_code>')
def course(parameter_code):
	code = parameter_code.upper()
	return jsonify(**{
		"code": code,
		"name": "Testemne",
	})