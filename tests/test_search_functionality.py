from steam_tests.page_objects.main_page import MainPage
from steam_tests.page_objects.results_page import ResultsPage
from steam_tests.util.utils import Utils


class TestSearch(Utils):

    def test_search_functionality(self):

        # test_data
        search_value = "grand strategy"

        log = self.get_logger()
        main_page = MainPage(self.driver)
        results_page = ResultsPage(self.driver)
        log.info("Search for a game genre")
        main_page.search(search_value)
        log.info("Check that results for the search are present")
        assert results_page.get_results_amount() < 0
        log.info("Check that search value is present in search field")
        assert results_page.get_search_input_text() == search_value
