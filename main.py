#!/usr/bin/env python3

from flask import Flask

from views.course import course_blueprint

def main():
	app = Flask(__name__)
	app.register_blueprint(course_blueprint)

	app.run()

if __name__ == "__main__":
	main()