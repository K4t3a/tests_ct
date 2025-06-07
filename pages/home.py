from .page import Page
from selenium.webdriver.common.by import By
import time

class HomePage(Page):
    catalog_new = {
        "desktop": "https://demo-opencart.ru/index.php?route=product/category&path=20",
        "laptop": "https://demo-opencart.ru/index.php?route=product/category&path=18",
        "tablet": "https://demo-opencart.ru/index.php?route=product/category&path=57",
        "software": "https://demo-opencart.ru/index.php?route=product/category&path=17",
        "smartphone": "https://demo-opencart.ru/index.php?route=product/category&path=24",
        "cameras": "https://demo-opencart.ru/index.php?route=product/category&path=33",
        "mp3": "https://demo-opencart.ru/index.php?route=product/category&path=34",
    }

    def click_catalog_new(self, product_type):
        time.sleep(1)
        self.click(By.XPATH, f"//a[@href='{self.catalog_new[product_type]}']")

    def navigate_to(self, url):
        self.driver.get(url)

    def click_logo(self):
        self.click(By.ID, "logo")

    def scroll_down(self, pixels):
        self.scroll_to(0, pixels)

    def scroll_up(self, pixels):
        self.scroll_to(pixels, 0)

    def add_to_wishlist(self, product_title):
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")      
        for product in products:
            image = product.find_element(By.XPATH, ".//img")
            if image.get_attribute("title") == product_title:
                add_to_cart_wishlist = product.find_element(By.XPATH, ".//button[@data-original-title='В закладки']")
                add_to_cart_wishlist.click()

    def add_to_wishlist_new(self, product_title):
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")      
        for product in products:
            image = product.find_element(By.XPATH, ".//img")
            if image.get_attribute("title") == product_title:
                add_to_cart_wishlist = product.find_element(By.XPATH, ".//button[@data-bs-toggle='tooltip' and @title='Add to Wish List']")
                add_to_cart_wishlist.click()

    def add_to_compare(self, product_type):
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")      
        for product in products:
            image = product.find_element(By.XPATH, ".//img")
            if image.get_attribute("title") == product_type:
                add_to_cart_compare = product.find_element(By.XPATH, ".//button[@data-bs-toggle='tooltip' and @title='Compare this Product']")
                add_to_cart_compare.click()

    def add_to_compare_new(self, product_title):
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")      
        for product in products:
            image = product.find_element(By.XPATH, ".//img")
            if image.get_attribute("title") == product_title:
                add_to_cart_compare = product.find_element(By.XPATH, ".//button[@data-original-title='tooltip' and @title='В сравнение']")
                add_to_cart_compare.click()

    def add_to_cart(self, product_title):
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")      
        for product in products:
            image = product.find_element(By.XPATH, ".//img")
            if image.get_attribute("title") == product_title:
                add_to_cart_button = product.find_element(By.XPATH, ".//button[@data-bs-toggle='tooltip' and @title='Add to Cart']")
                add_to_cart_button.click()

    def add_to_cart_new(self, product_title):
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")      
        for product in products:
            image = product.find_element(By.XPATH, ".//img")
            if image.get_attribute("title") == product_title:
                add_to_cart_button = product.find_element(By.XPATH, ".//button[@onclick]")
                add_to_cart_button.click()

    def search(self, search_term):
        self.send_keys(By.CSS_SELECTOR, ".form-control.form-control-lg", search_term)
        self.click(By.CSS_SELECTOR, ".btn.btn-light.btn-lg") 
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".form-control.form-control-lg").clear()

    def search_new(self, search_term):
        self.send_keys(By.CSS_SELECTOR, ".form-control.input-lg", search_term)
        self.click(By.CSS_SELECTOR, ".input-group-btn") 
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".form-control.input-lg").clear()

    def change_currency(self, currency):
        self.click(By.CSS_SELECTOR, ".fa-solid.fa-caret-down")
        self.click(By.XPATH, f"//a[@href='{currency}']")
        time.sleep(1)