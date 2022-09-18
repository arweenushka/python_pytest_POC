import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    """ Function added from official doc to be able to use command line options"""
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setUp(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        #add path to chromedriver here
        # driver = webdriver.Chrome(executable_path="/Users/barysmar/Documents/qa/python_selenium/basic_course/chromedriver")
        driver = webdriver.Chrome()  # for mac is taken path automatically
    elif browser_name == "firefox":
        pass
        # add another driver if you want
    driver.get("https://store.steampowered.com/")
    driver.maximize_window()
    # TODO move to tear_down method
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)