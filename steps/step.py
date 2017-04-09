# -*- coding: utf-8 -*-
from behave import *
From selenium import web driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given('website "{url}"')
def step(context, url):
#Открываем браузер
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()
    context.browser.get("http://ya.ru")

#Нажимаем в поиске "Найти"
@then("push button with text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//button'))
    )
    context.browser.find_element_by_xpath('//button').click()

#Проверка что мы на странице с нужным текстом
@then("page include text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    )
    assert context.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
    context.browser.quit()
