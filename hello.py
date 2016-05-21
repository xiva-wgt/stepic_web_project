#!/usr/bin/python
import urlparse

def app_start(environ, start_response):
    response_body = b''
    dict_with_query_string = urlparse.parse_qs(environ.get('QUERY_STRING', ''), keep_blank_values=True)
    for item in dict_with_query_string:
        for item_value in dict_with_query_string[item]:
            response_body += b'{0}={1}\n'.format(item, item_value)
    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
    ]

    start_response(status, response_headers)

    return [response_body]

