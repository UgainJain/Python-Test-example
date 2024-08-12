# 3213852



## DemoStore Authomation With Python

This project is based for testing DemoStore website using python  



## Prerequisites

- Python 3.x
- `pip` package manager
```

## Setup

1. Clone the repository:

    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:

    ```sh
    pip install selenium
    pip istall pytest
    pip install pytest--html
    ```

## Running the Tests

1. To run all tests and generate an HTML report:

    ```sh
    pytest --html=reports/report.html --self-contained-html
    ```

2. To run specific tests (e.g., signup tests):

    ```sh
    pytest tests/test_login.py
    ```
3. The screenshots are generated for all failed tests and are in screeshot folder.
  

## Test Data

Test data is stored in JSON files within the `Test_data` directory. Each test file reads data from its corresponding JSON file

Example of `test_data_login.json`:

```json
[
   
  {
    "name": "Mpho",
    "country": "USA",
    "city": "MiaMi",
    "card": 1234455665667,
    "month": "April",
    "year": 2025
  }
]
```

## Project features
 -  Fixtures  provide a way to define setup and teardown code that is shared across multiple test cases.Implemented for  setting up browser and invoked in each test class
 -  Hooks  functions that are called at some points in tests,implemented for taking screenshots when test fails and for       configuring/generating logs
 -  selenium  used to automate the website
 -  pytest  testing framework which allows us to write test code using python

