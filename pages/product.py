from .page import Page
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(Page):
    def select_prod(self, product_title):
        products = self.driver.find_elements(By.CSS_SELECTOR, ".product-thumb.transition")      
        for product in products:
            title_element = product.find_element(By.XPATH, ".//h4/a")
            if title_element.text.strip() == product_title.strip():
                self.driver.execute_script("arguments[0].scrollIntoView(true);", title_element)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//h4/a")))
                title_element.click()
                break
        else:
            raise Exception(f"Product {product_title} not found")

    def add_to_wishlist(self):
        self.click(By.CSS_SELECTOR, "button[data-original-title='В закладки']")

    def add_to_wishlist_new(self):
        self.click(By.CSS_SELECTOR, "button[data-original-title='В закладки']")

    def select_color(self, color_value):
        self.click(By.ID, "input-option-226")
        self.click(By.CSS_SELECTOR, f"[value='{color_value}']")

    def add_to_cart(self):
        self.click(By.ID, "button-cart")