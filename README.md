# Pytest Tutorial

`pytest` is a open-source testing Framework based on Python that is mainly used to write and execute test code. This tutorial is inspired by [Tutorialspoint](https://www.tutorialspoint.com/pytest/index.htm). `pytest` is mainly used for API testing although you can pretty much use it to write complex tests i.e UI, db and so forth.

*Some advantages of `pytest`.*

* run multiple test at once thus reducing execution time of a testing suite.
* built-in way to automatically detect test files and tests if not mentioned explicitly.
* can skip or run a subset of tests during execution.

In this tutorial, we will touch on the following topics.

* installing `pytest`.
* identifying test files and test functions.
* executing all test files.
* executing specific file.
* execute tests by substring match.
* execute tests based on markers.
* creating fixtures.
* `conftest.py` allows accessing fixtures from multiple files.
* parametrizing tests.
* xfailing tests.
* skipping tests.
* stop test execution on nth failures.
* running tests in parallel.
* generating results in xml and html.

## Environment set-up

Ensure that you have `python` installed that you have setup virtual environment for this tutorial by installing `python3-venv` package.

Pull the git repository.

``` bash
git pull git@github.com:ymkl/pytest-tutorial.git
cd pytest-tutorial
```

Create a Python environment.

``` python
python3 -m venv <env_name>
```

Install the needed modules i.e `pytest`, `pytest` and so forth using the `requirements.txt` file.

``` python
pip3 install -r requirements.txt
```

## Getting our hands dirty

`pytest` automatically picks up files in the currect/sub directory that have the prefix or suffix of `test_*.py` or `*_test.py`, respectively, unless stated explicitly which files to run. And, it requires test function names to start with `test` otherwise it won't treat those functions as test functions and this applies to classes.

Running tests.

``` python
pytest -v # execute all tests in verbose mode
pytest <filename> -v # to execute specific test file
```

You can run a subset of a test suite by either selecting tests to run based on substring matching test names or run based on the markers applied to them. Markers set various features/attributes to test functions along with some builtin markers but users can also create their own markers as well.

``` python
# Substring of test names
pytest -k <substring> -v

# Create a marker
@pytest.mark.<markername>

# Use the marker
pytest -m <markername> -v
```

Fixtures are functions that run before tests to feed them with data i.e db connections. You can simply attach a fixture to a test enabling code re-use. You pass the fixture as a input parameter to the test allowing you to apply it to as many test as needed. A fixture within a test file has a scope is limited to that file and cannot be used outside it. In order to enable this, we need to use `conftest.py` file. How it works is, the test will look for the fixture in the file if it's not found, it will look at the `conftest.py` file, invoke the fixture, then the results are passed as input arguments to the test.

``` python
# Fixture definition
@pytest.fixture
def input_val():
    return 33

# fixture use
def test_divisible_by_3(input_val):
    assert input_val % 3 = 0
```

If you want to run a test against multiple input, you can make use of `parameterizing`.

``` python
# Parameterizing marker
@pytest.mark.parametrize
```

We can `skip` testas needed and `xfail` them -> `pytest` will execute the tests but will not be considered as passed or failed and results won't be returned.

``` python
# xfail marker
@pytest.mark.xfail

# skip marker
@pytest.mark.skip
```

We can set a test suite to fail after a certain number of failures during execution.

``` python
pytest --maxfail=<num>
```

By definition, `pytest` runs testin sequential order which in turn might slow down execution time of larger test suites. To mitigate this, you can run your tests in parallel, but first, install:

``` python
pip3 install pytest-xdist

# Then
pytest -v -n 3 # this will run your tests with 3 workers
```

You can generate the details of your tests with either using `XML` or `HTML` and pass this info to dashboards/tools that you're using in your infrastructure.

``` python
# XML export
pytest -v --junitxml=report.xml

# HTML export
# Install pytest-html, which is already installed for by the requirements.txt file
pip3 install pytest-html
pytest -v --html=report.html
```
