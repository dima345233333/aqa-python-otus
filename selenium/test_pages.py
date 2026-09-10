import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re


def test_popular_products(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(driver=browser, timeout=10)

    home_page = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    assert home_page.is_displayed(), "Home page not displayed"

    carousel = wait.until(EC.visibility_of_element_located((By.ID, "carousel")))
    assert carousel.is_displayed(), "Not found carousel"

    popular_title = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".products-section-title"))
    )
    assert popular_title.is_displayed(), "Not found popular"

    products_section = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".featured-products"))
    )
    products = products_section.find_elements(By.CSS_SELECTOR, ".js-product.product")
    assert len(products) == 8, f"Expected 8 products, found {len(products)}"

    banner = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.banner")))
    assert banner.is_displayed(), "Not found banner"


def test_art_page(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(driver=browser, timeout=10)

    art_button = wait.until(EC.visibility_of_element_located((By.ID, "category-9")))
    art_link = art_button.find_element(By.CLASS_NAME, "dropdown-item")
    assert art_link.is_displayed(), "Not found Art link"

    art_link.click()
    wait.until(EC.url_to_be(f"{base_url}/9-art"))
    assert browser.current_url == f"{base_url}/9-art"

    filters = wait.until(EC.visibility_of_element_located((By.ID, "search_filters")))
    assert filters.is_displayed(), "Not found filters"

    div_info = wait.until(
        EC.visibility_of_element_located((By.ID, "js-product-list-header"))
    )
    assert div_info.is_displayed(), "Not found block with info"

    expected_count = 0
    total_products_text = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".total-products p"))
    )
    text = total_products_text.text
    numbers = re.findall(r"\d+", text)
    if numbers:
        expected_count = int(numbers[0])
    products = browser.find_elements(By.CSS_SELECTOR, ".js-product.product")
    actual_count = len(products)
    assert actual_count == expected_count, "Not found all зкщвгсеы"


def test_product_card(browser, base_url):
    browser.get(
        f"{base_url}/men/1-1-hummingbird-printed-t-shirt.html#/1-size-s/8-color-white"
    )
    wait = WebDriverWait(driver=browser, timeout=10)

    image = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-cover img"))
    )
    assert image.is_displayed(), "Not found product image"

    title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.h1")))
    assert title.is_displayed(), "Not found product title"

    price = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".current-price-value"))
    )
    assert price.is_displayed(), "Not found product price"

    size_dropdown = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#group_1"))
    )
    assert size_dropdown.is_displayed(), "Not found size"

    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart")))
    assert button.is_displayed(), "Not found add to cart button"


def test_admin_panel(browser, base_url):
    browser.get(f"{base_url}/administration")
    wait = WebDriverWait(driver=browser, timeout=10)

    mail_field = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    assert mail_field.is_displayed(), "Not found email field"

    password_field = wait.until(EC.visibility_of_element_located((By.ID, "passwd")))
    assert password_field.is_displayed(), "Not found password field"

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "submit_login")))
    assert login_button.is_displayed(), "Not found login button"

    checkbox = wait.until(EC.visibility_of_element_located((By.ID, "stay_logged_in")))
    assert checkbox.is_displayed(), "Not found stay logged in checkbox"

    forgot_password_link = wait.until(
        EC.visibility_of_element_located((By.ID, "forgot-password-link"))
    )
    assert forgot_password_link.is_displayed(), "Not found forgot password link"

    assert "I forgot my password" in forgot_password_link.text


def test_register_panel(browser, base_url):
    browser.get(f"{base_url}/registration")
    wait = WebDriverWait(driver=browser, timeout=10)

    first_name = wait.until(
        EC.visibility_of_element_located((By.ID, "field-firstname"))
    )
    assert first_name.is_displayed(), "Not found first name field"

    last_name = wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
    assert last_name.is_displayed(), "Not found last name field"

    mail = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
    assert mail.is_displayed(), "Not found email field"

    password = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
    assert password.is_displayed(), "Not found password field"

    save_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    assert save_button.is_displayed(), "Not found save button"
