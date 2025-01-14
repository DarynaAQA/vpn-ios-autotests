from base_classes.appium_methods import AppiumMethods
from locators.server_select_locators import ServerSelectLocators


class ServerSelectPage(AppiumMethods):
    def add_server_to_favorites(self):
        return self.is_clickable('accessibility_id', ServerSelectLocators.AddAlbaniaToFavorites).click()

    def favorites_servers_click(self):
        return self.is_clickable('accessibility_id', ServerSelectLocators.Favorites).click()

    def check_for_presence_albania_server(self):
        return self.is_present('accessibility_id', ServerSelectLocators.AlbaniaServer)

    def check_presence_for_finland_server(self):
        return self.is_present('accessibility_id', ServerSelectLocators.FinlandServer)

    def check_presence_for_new_york_server(self):
        return self.is_present('accessibility_id', ServerSelectLocators.NewYorkServer)

    def server_search_click(self):
        return self.is_clickable('class_name', ServerSelectLocators.ServerSearch).click()






