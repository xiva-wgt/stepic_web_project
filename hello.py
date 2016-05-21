#!/usr/bin/python
import urlparse


def application(environ, start_response):
    response_body = b''
    dict_with_query_string = urlparse.parse_qs(environ.get('QUERY_STRING', ''), keep_blank_values=True)
    for item in dict_with_query_string:
        for item_value in dict_with_query_string[item]:
            response_body += b'{0}={1}\n'.format(item, item_value)
    status = '200 OK'
    start_response(status, [('Content-Type', 'text/plain')])
    return [response_body]


