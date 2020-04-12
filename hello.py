import re


def app(env, start_response):
    query_string = env["QUERY_STRING"]
    ans = '\n'.join(re.findall(r'([^?=&]+=[^&]*)+', query_string))
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [ans]

