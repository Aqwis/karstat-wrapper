import requests
from urllib.parse import urlparse, parse_qs

import settings

def is_page_feide_login(html):
	return "SSO wrapper" in html

def login():
	URL = 'http://sats.itea.ntnu.no/sso-wrapper/feidelogin?RelayState=%2Fsso-wrapper%2Fweb%2Fwrapper%2F%3Ftarget%3DKarstatProd'
	response = requests.get(URL)

	html = response.text
	new_URL = response.url

	assert response.status_code == 200
	assert is_page_feide_login(html)

	parsed_new_URL = urlparse(new_URL)
	query_parameters = parse_qs(parsed_new_URL.query)
	post_form_data = query_parameters

	post_form_data['feidename'] = settings.FEIDE_USERNAME
	post_form_data['password'] = settings.FEIDE_PASSWORD
	post_form_data['org'] = 'ntnu.no'
	post_form_data['has_js'] = '0'
	post_form_data['inside_iframe'] = '0'
	post_form_data['asLen'] = str(post_form_data['asLen'][0])
	post_form_data['AuthState'] = post_form_data['AuthState'][0]

	print(post_form_data)

	response = requests.post(new_URL, data=post_form_data, cookies=response.cookies, allow_redirects=True)
	new_html = response.text

	for r in response.history + [response]:
		print(r.status_code)
		print(r.url)

	return ('Karakterstatistikk' in new_html, response.cookies)