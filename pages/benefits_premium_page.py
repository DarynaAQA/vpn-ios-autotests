from base_classes.appium_methods import AppiumMethods
from locators.benefits_premium_locators import BenefitPremiumLocators


class BenefitsPremiumPage(AppiumMethods):
    def select_plan_click(self):
        return self.is_clickable('accessibility_id', BenefitPremiumLocators.SelectPlan).click()
