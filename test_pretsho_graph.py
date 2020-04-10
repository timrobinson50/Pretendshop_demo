import requests
import json
import pytest

def pretty_print_request(request):
    print( '\n{}\n{}\n\n{}\n\n{}\n'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body)
    )

def pretty_print_response(response):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text)
    ) 

def test_post_headers_body_json(supply_url):

    #url = "http://pretendshop.herokuapp.com/v1/graphql"
    url = supply_url

    payload = "{\"query\":\"query MyQuery {\\n  Jobs {\\n    Job_title\\n    id\\n  }\\n}\",\"variables\":{}}"
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))


    # print full request and response
    pretty_print_request(response.request)
    pretty_print_response(response)

    # Validate response headers and body contents, e.g. status code.
    print("** Test 1: Validating status response code **")
    assert response.status_code == 200
    print("Response is 200 - Test PASS")


def test_jobs_json():

    url = "http://pretendshop.herokuapp.com/v1/graphql"

    payload = "{\"query\":\"query MyQuery {\\n  Jobs {\\n    Job_title\\n    id\\n  }\\n}\",\"variables\":{}}"
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    # print(response.text.encode('utf8'))


    # print full request and response
    # pretty_print_request(response.request)
    # pretty_print_response(response)

    # Validate response headers and body contents, e.g. status code.
    #print("Test 1: Validating status response code")
    #assert response.status_code == 200
    #print("Response is 200 - Test PASS")

    resp_body = response.json()
    resp_jobs = resp_body["data"]
    #resp_jobtitles = resp_jobs["Job_title"]
    #assert resp_body['url'] == url
    print(resp_body)
    print()
    print(resp_jobs)
    print()
    print(resp_jobs['Jobs'])
    #print(resp_jobs['Jobs'][0])
    print()
    print("** Test 2: Checking jobs **")
    for job in resp_jobs['Jobs']:
        print(job)
        assert job
        print("Job found - Test PASS")

print("** Testing complete... ***")