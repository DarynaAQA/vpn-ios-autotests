from base_classes.appium_methods import AppiumMethods
from locators.sidebar_subscriptions_locators import SubscriptionsLocators


class SubscriptionsPage(AppiumMethods):

    def check_for_presence_one_year(self):
        return self.is_present('accessibility_id', SubscriptionsLocators.OneYear)

    def check_for_presence_six_months(self):
        return self.is_present('accessibility_id', SubscriptionsLocators.SixMonths)

    def check_for_presence_one_month(self):
        return self.is_present('accessibility_id', SubscriptionsLocators.OneMonth)

    def check_for_presence_premium_subscription_title(self):
        return self.is_present('name', SubscriptionsLocators.PremiumSubscriptionTitle)

    def check_for_presence_subscription_title(self):
        return self.is_present('name', SubscriptionsLocators.PremiumSubscriptionTitle)





