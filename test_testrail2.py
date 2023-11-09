#!/usr/bin/env python
"""
This script tests basic functionalities of `testrail2.py`.

Preconditions:
- An active TestRail instance
- User with permissions to:
    - Create Projects, Suites, Tests and Runs
- An API key

It tests:
- Creating a ...
    - project
    - suite
    - section
    - test case
    - test run
- Get runs
- Add an attachment to a run
- Show an attachments inside a run
"""
import testrail2 as tr2


class TRApiTest:
    def __init__(self):
        self.base_url = 'https://<URL>.testrail.io'
        self.api = tr2.APIClient(self.base_url)
        self.api.user = '<USER>'
        self.api.password = '<API KEY>'

    def go(self, uri: str, data=None):
        if uri.startswith('get'):
            return self.api.send_get(uri)
        elif uri.startswith('add'):
            return self.api.send_post(uri, data)


def test_run_json(test_suite_id):
    return {
        "suite_id": test_suite_id,
        "name": "This is a new test run",
        "include_all": True
    }


def test_section_json(test_suite_id):
    return {
        "suite_id": test_suite_id,
        "name": "This is a new section"
    }


def test_case_json(test_section_id):
    return {
        "section_id": test_section_id,
        "title": "Testing an API"
    }


test_project_json = {
    "name": "Project X",
    "announcement": "Welcome to project X",
    "show_announcement": False
}

test_suite_json = {
    "name": "This is a new test suite",
    "description": "Use the description to add additional context details"
}

test_file = 'test.json'


if __name__ == '__main__':
    tr_api = TRApiTest()

    # Creating a new project
    test_add_project = tr_api.go('add_project', test_project_json)
    project_id = test_add_project['id']

    # Creating a new suite, based on the project ID
    test_add_suite = tr_api.go(f'add_suite/{project_id}', test_suite_json)
    suite_id = test_add_suite['id']

    # Add a section to a suite
    test_add_section = tr_api.go(f'add_section/{project_id}', test_section_json(suite_id))
    section_id = test_add_section['id']

    # Add a test case to a suite
    test_add_case = tr_api.go(f'add_case/{section_id}', test_case_json(section_id))
    case_id = test_add_case['id']

    # Create a new test run
    test_add_run = tr_api.go(f'add_run/{project_id}', test_run_json(suite_id))
    run_id = test_add_run['id']

    # Get run
    test_get_runs = tr_api.go(f'get_runs/{project_id}')

    # Add attachment to a run
    test_add_attachment_run = tr_api.go(f'add_attachment_to_run/{run_id}', test_file)

    # Show all attachments in a run
    test_get_attachment_run = tr_api.go(f'get_attachments_for_run/{run_id}')

    print(test_add_project)
    print(test_add_suite)
    print(test_add_section)
    print(test_add_case)
    print(test_add_run)
    print(test_get_runs)
    print(test_add_attachment_run)
    print(test_get_attachment_run)
