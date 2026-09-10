import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random
import re


def test_admin_authorization(browser, base_url):
    ADMIN_MAIL = "admin@example.com"
    ADMIN_PASSWD = "Admin123!"

    browser.get(f"{base_url}/administration")
    wait = WebDriverWait(driver=browser, timeout=10)

    mail_field = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    assert mail_field.is_displayed(), "Not found email field"
    mail_field.send_keys(ADMIN_MAIL)

    password_field = wait.until(EC.visibility_of_element_located((By.ID, "passwd")))
    assert password_field.is_displayed(), "Not found password field"
    password_field.send_keys(ADMIN_PASSWD)

    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit_login")))
    submit_button.click()

    tab_dashboard = wait.until(
        EC.visibility_of_element_located((By.ID, "tab-AdminDashboard"))
    )
    assert tab_dashboard.is_displayed(), "Not found tab-AdminDashboard"

    tab_orders = wait.until(
        EC.visibility_of_element_located((By.ID, "subtab-AdminParentOrders"))
    )
    assert tab_orders.is_displayed(), "Not found subtab-AdminParentOrders"

    tab_customer = wait.until(
        EC.visibility_of_element_located((By.ID, "subtab-AdminParentCustomer"))
    )
    assert tab_customer.is_displayed(), "Not found subtab-AdminParentCustomer"

    tab_payment = wait.until(
        EC.visibility_of_element_located((By.ID, "subtab-AdminParentPayment"))
    )
    assert tab_payment.is_displayed(), "Not found subtab-AdminParentPayment"

    employee_info = wait.until(EC.element_to_be_clickable((By.ID, "employee_infos")))
    employee_info.click()

    logout_button = wait.until(EC.element_to_be_clickable((By.ID, "header_logout")))
    logout_button.click()

    mail_field = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    assert mail_field.is_displayed(), "Not found email field"

    password_field = wait.until(EC.visibility_of_element_located((By.ID, "passwd")))
    assert password_field.is_displayed(), "Not found password field"


def test_random_item(browser, base_url):

    browser.get(base_url)
    wait = WebDriverWait(driver=browser, timeout=10)

    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".featured-products .js-product")
        )
    )
    assert len(products) > 0, "Not found products on page"

    random_product = random.choice(products)

    product_link = random_product.find_element(
        By.CSS_SELECTOR, ".thumbnail.product-thumbnail"
    )
    product_link.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".add-to-cart")))

    add_to_cart_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button.add-to-cart[data-button-action="add-to-cart"]')
        )
    )
    add_to_cart_button.click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#blockcart-modal")))

    continue_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[contains(text(), "Continue shopping")]')
        )
    )
    continue_button.click()

    cart_link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#_desktop_cart .blockcart a"))
    )
    cart_link.click()

    cart_items = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cart-item"))
    )
    assert len(cart_items) > 0, "Not found products in cart"

    product_name_in_cart = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-line-info a"))
    )
    assert product_name_in_cart.is_displayed(), "Not found product name in cart"


def test_switch_currencies_popular(browser, base_url):

    browser.get(base_url)
    wait = WebDriverWait(driver=browser, timeout=10)

    price_element = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".product-price-and-shipping .price, .price")
        )
    )
    eur_price_text = price_element.text.strip()
    assert "€" in eur_price_text, f"Not found EUR symbol in {eur_price_text}"

    currency_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'button[data-toggle="dropdown"][aria-label="Currency dropdown"]',
            )
        )
    )
    currency_button.click()

    usd_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "USD $")]'))
    )
    usd_option.click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".product-price-and-shipping .price, .price"), "$"
        )
    )

    new_price_element = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".product-price-and-shipping .price, .price")
        )
    )
    usd_price_text = new_price_element.text.strip()
    assert "$" in usd_price_text, f"Not found USD symbol in {usd_price_text}"


def test_switch_currencies_catalog(browser, base_url):
    browser.get(f"{base_url}/3-clothes")
    wait = WebDriverWait(driver=browser, timeout=10)

    price_element = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".product-price-and-shipping .price, .price")
        )
    )
    eur_price_text = price_element.text.strip()
    assert "€" in eur_price_text, f"Not found EUR symbol in {eur_price_text}"

    currency_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                'button[data-toggle="dropdown"][aria-label="Currency dropdown"]',
            )
        )
    )
    currency_button.click()

    usd_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "USD $")]'))
    )
    usd_option.click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".product-price-and-shipping .price, .price"), "$"
        )
    )

    new_price_element = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".product-price-and-shipping .price, .price")
        )
    )
    usd_price_text = new_price_element.text.strip()
    assert "$" in usd_price_text, f"Not found USD symbol in {usd_price_text}"
