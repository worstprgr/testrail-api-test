# Testing the bindings for `testrail2.py`
This is a separate test demo for the modified variant of the original `testrail.py`.  
https://github.com/worstprgr/testrail-api/blob/master/python/3.x/testrail2.py

## Running the test
### Preconditions
- An active TestRail instance
- User with permissions to:
    - Create Projects, Suites, Tests and Runs
- An API key  
- The `testrail2.py` file in the same folder, like the test script  

### Inside the script
Adjust the following variables:  
```python
self.base_url = 'https://<URL>.testrail.io'
self.api.user = '<USER>'
self.api.password = '<API KEY>'
```

### Run
`python test_testrail2.py`


## Test Scope
- Creating a ...
    - project
    - suite
    - section
    - test case
    - test run
- Get runs
- Add an attachment to a run
- Show an attachments inside a run
