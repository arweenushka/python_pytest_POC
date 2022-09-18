# POC of test automation project using python with pytest framework

Tests check that search functionality and menu bar are working. Logging, reporting and screenshots on failure are added. Projects based on Page Object concept. 

No changes needed if project executes on Mac with chromedriver installed. If not, please install chromedriver or add updated version to the project folder and change chromedriver path in conftest.py file

python version is 3.10.6

# How to run?
Open cmd in the project folder and run the command 

All test 

    > py.test
    
All test with report

    > py.test --html=report.html


# Notes for pytest

- Any pytest file should start with test_ or end with _test
- pytest method names should start with test
- Any code should be wrapped in method only
- Method name should have sense
- -k stands for method names execution, -s logs in out put  -v stands for more info metadata
- you can run specific file with py.test <filename>
- you can mark (tag) tests @pytest.mark.smoke and then run with -m
- you can skip tests with @pytest.mark.skip
- Pytest will execute the xfailed test, but it will not be considered as part failed or passed tests. Details of these tests will not be printed even if     the test fails @pytest.mark.xfail
- fixtures are used as setup and tear down methods for test cases- conftest file to generalize fixture
  and make it available to all test cases (fixture name into parameters of method)
- datadriven and parameterization can be done with return statements in tuple format
- when you define fixture scope to class only, it will run once before class is initiated and at the end
