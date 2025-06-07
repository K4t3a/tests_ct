from .page import Page
from selenium.webdriver.common.by import By

class ReviewPage(Page):
    def click_review(self):
        self.click(By.XPATH, "//a[@href='#tab-review']")
    def write_review(self, name, text, rating):
        self.send_keys(By.ID, "input-name", name)
        self.send_keys(By.ID, "input-text", text)
        self.click(By.CSS_SELECTOR, f"[value='{rating}']")
        self.click(By.ID, "button-review")