import requests



def follow_redirect(_session, _url, _headers = '', _data = '', _params = '', _):
    _req = _session.post(url, headers=_headers, data=_data)
    if _req.status_code in [301,302]:
        jar = _req.cookies
        redirect = _req.headers['Location']
        redirected = _session.get(redirect, cookies=jar)
        return _session, _redirected