import requests
import re
import time
from random import randint

def get_random_user_agent():
    	user_agent_array = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
	'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36']
	value = randint(0,len(user_agent_array) - 1)
	return user_agent_array[value]


def follow_redirect(_session, _url, _headers = '', _data = '', _params = '', _ = ''):
    _req = _session.post(url, headers=_headers, data=_data)
    if _req.status_code in [301,302]:
        jar = _req.cookies
        redirect = _req.headers['Location']
        redirected = _session.get(redirect, cookies=jar)
        return _session, _redirected

def get_headers():
    	return {
			"accept": "application/json",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "en-US,en;q=0.9",
			"content-type": "application/json",
			"pragma":"no-cache",
			"sec-fetch-mode":"cors",
			"sec-fetch-site":"same-origin",
			"User-Agent": get_random_user_agent()
			}

def regex_finds(pattern_text, search_string, console_print = False):
    	_pattern = "{}".format(pattern_text)
	_search = re.findall(_pattern, search_string)
	return _search



