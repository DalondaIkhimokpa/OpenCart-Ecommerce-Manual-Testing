# test_opencart_checkout.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_guest_checkout_flow():
    driver = webdriver.Chrome()
    driver.get("http://your-opencart-demo-url.com")

    # Search for a product
    driver.find_element(By.NAME, "search").send_keys("Laptop")
    driver.find_element(By.CSS_SELECTOR, ".btn-default").click()

    # Add first product to cart
    driver.find_element(By.CSS_SELECTOR, ".product-layout .button-group button").click()
    time.sleep(2)

    # Go to cart
    driver.find_element(By.ID, "cart-total").click()
    driver.find_element(By.LINK_TEXT, "View Cart").click()

    # Proceed to checkout
    driver.find_element(By.LINK_TEXT, "Checkout").click()
    time.sleep(2)

    assert "Checkout" in driver.title
    driver.quit()
