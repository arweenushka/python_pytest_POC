from steam_tests.page_objects.main_page import MainPage
from steam_tests.util.utils import Utils


class TestMenuBar(Utils):

    def test_menu_bar(self):

        # test_data
        menu_bar_element_name = "Categories"
        menu_bar_sub_element_name = "Action RPG"

        log = self.get_logger()
        main_page = MainPage(self.driver)
        log.info("Check that element is present in menu bar")
        assert menu_bar_sub_element_name in main_page.get_sub_menu_bar_elements_list(menu_bar_element_name), \
            "This sub element from menu bar is not exist "
